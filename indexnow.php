<?php
// Kilómetro Real · avisa a IndexNow (Bing, DuckDuckGo, Yandex...) de las URLs nuevas del sitemap.
// Solo envía URLs que no se han enviado antes, más la portada, el precio de la gasolina y las noticias recientes.
// Se puede llamar las veces que se quiera: si no hay nada nuevo, no envía nada.
header('Content-Type: text/plain; charset=utf-8');
header('X-Robots-Tag: noindex');
$key  = '__INDEXNOW_KEY__';
$host = 'kilometroreal.com';
$dir  = __DIR__;
$state = dirname($dir) . '/.kr-indexnow-sent.txt'; // fuera de public_html
$lock  = dirname($dir) . '/.kr-indexnow-last.txt';
if (file_exists($lock) && time() - (int)@file_get_contents($lock) < 600) { echo "Espera: ya se envió hace menos de 10 minutos.\n"; exit; }
$locs = function ($f) use ($dir) { $x = @file_get_contents("$dir/$f"); if (!$x) return []; preg_match_all('#<loc>([^<]+)</loc>#', $x, $m); return $m[1]; };
$all  = array_values(array_unique(array_merge($locs('sitemap.xml'), $locs('news-sitemap.xml'))));
$sent = file_exists($state) ? array_flip(array_filter(explode("\n", file_get_contents($state)))) : [];
$always = array_merge(["https://$host/", "https://$host/precio-gasolina-hoy/", "https://$host/noticias/"], $locs('news-sitemap.xml'));
$todo = [];
foreach ($all as $u) if (!isset($sent[$u])) $todo[] = $u;
if ($sent) $todo = array_merge($todo, $always);
$todo = array_slice(array_values(array_unique($todo)), 0, 10000);
if (!$todo) { echo "Nada nuevo que enviar.\n"; exit; }
$body = json_encode(['host' => $host, 'key' => $key, 'keyLocation' => "https://$host/$key.txt", 'urlList' => $todo], JSON_UNESCAPED_SLASHES);
$ch = curl_init('https://api.indexnow.org/indexnow');
curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_POSTFIELDS => $body, CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTPHEADER => ['Content-Type: application/json; charset=utf-8']]);
$res = curl_exec($ch); $code = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
file_put_contents($lock, time());
if ($code == 200 || $code == 202) {
  file_put_contents($state, implode("\n", array_keys($sent + array_flip($all))));
  echo "OK $code: enviadas " . count($todo) . " URLs.\n";
} else { echo "Error $code: $res\n"; }
