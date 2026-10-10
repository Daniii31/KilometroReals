<?php
// Kilómetro Real · formulario de contacto. Envía el mensaje al buzón del sitio.
header('Content-Type: application/json; charset=utf-8');
header('X-Robots-Tag: noindex');

$TO   = '__CONTACT_EMAIL__';
$FROM = 'noreply@kilometroreal.com';
$en   = (($_POST['lang'] ?? '') === 'en');
function fail($msg, $code = 400) { http_response_code($code); echo json_encode(['ok' => false, 'error' => $msg]); exit; }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') fail($en ? 'Method not allowed.' : 'Método no permitido.', 405);
if (!empty($_POST['website'])) { echo json_encode(['ok' => true]); exit; } // trampa antispam
// el formulario se envía desde nuestra web
$orig = $_SERVER['HTTP_ORIGIN'] ?? ($_SERVER['HTTP_REFERER'] ?? '');
if ($orig !== '' && !preg_match('#^https?://(www\.)?kilometroreal\.com#i', $orig)) fail($en ? 'Not allowed.' : 'No permitido.', 403);
// trampa de tiempo: los bots rellenan en menos de 3 segundos
$secs = (int)($_POST['t'] ?? 0);   // segundos que la persona pasó en el formulario (lo calcula su navegador)
if ($secs < 3) { echo json_encode(['ok' => true]); exit; }

// límite: 3 mensajes cada 10 minutos por IP
$ip = $_SERVER['REMOTE_ADDR'] ?? 'x';
$f  = sys_get_temp_dir() . '/kr_contact_' . md5($ip);
$hits = array_filter(@json_decode(@file_get_contents($f), true) ?: [], fn($t) => $t > time() - 600);
if (count($hits) >= 3) fail($en ? 'Too many messages. Try again in a few minutes.' : 'Has enviado demasiados mensajes. Prueba en unos minutos.', 429);

$name    = trim(strip_tags($_POST['name'] ?? ''));
$email   = trim($_POST['email'] ?? '');
$topic   = preg_replace('/[^a-z]/', '', $_POST['topic'] ?? 'otro');
$message = trim(strip_tags($_POST['message'] ?? ''));
$consent = !empty($_POST['consent']);

if ($name === '' || mb_strlen($name) > 80) fail($en ? 'Please enter your name.' : 'Escribe tu nombre.');
if (!filter_var($email, FILTER_VALIDATE_EMAIL) || preg_match('/[\r\n]/', $email)) fail($en ? 'Enter a valid email address.' : 'Escribe un correo válido.');
if (mb_strlen($message) < 20 || mb_strlen($message) > 4000) fail($en ? 'The message must be between 20 and 4,000 characters.' : 'El mensaje debe tener entre 20 y 4.000 caracteres.');
if (preg_match_all('#https?://|www\.#i', $message) > 2) { echo json_encode(['ok' => true]); exit; } // demasiados enlaces = spam
if (preg_match('/[\x{0400}-\x{04FF}\x{4E00}-\x{9FFF}]{12,}/u', $message)) { echo json_encode(['ok' => true]); exit; }
if (!$consent) fail($en ? 'You need to accept the privacy policy.' : 'Tienes que aceptar la política de privacidad.');

$name = preg_replace('/[\r\n]+/', ' ', $name);
$subject = '=?UTF-8?B?' . base64_encode("[Kilómetro Real] $topic · $name") . '?=';
$body = "Nombre: $name\nCorreo: $email\nMotivo: $topic\nIdioma: " . ($en ? 'en' : 'es') . "\nIP: $ip\nFecha: " . date('c') . "\n\n$message\n";
$headers = "From: Kilómetro Real <$FROM>\r\nReply-To: $email\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\n";

if (!@mail($TO, $subject, $body, $headers, "-f$FROM")) fail($en ? 'It could not be sent. Please try again later.' : 'No se ha podido enviar. Prueba de nuevo más tarde.', 500);
$hits[] = time(); @file_put_contents($f, json_encode(array_values($hits)));
echo json_encode(['ok' => true]);
