<?php
// https://stackoverflow.com/a/9998628
ini_set('xdebug.var_display_max_depth', '10');
ini_set('xdebug.var_display_max_children', '256');
ini_set('xdebug.var_display_max_data', '1024');

$image_url = 'https://post.healthline.com/wp-content/uploads/2021/11/lotus-flower-in-pond-732x549-thumbnail-732x549.jpg';
$sizes = array(
    '200x300',
);

$api_credentials = array(
    'key' => 'acc_3484679611ff3db',
    'secret' => 'ba0a95b2d3e3b155664a5609013f5cec'
);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://api.imagga.com/v2/croppings?image_url=' . urlencode($image_url) . '&resolution=' . implode(',', $sizes));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($ch, CURLOPT_HEADER, FALSE);
curl_setopt($ch, CURLOPT_USERPWD, $api_credentials['key'].':'.$api_credentials['secret']);

$response = curl_exec($ch);
curl_close($ch);

$json_response = json_decode($response);
// var_dump($json_response);
echo '<pre>' . print_r($json_response, true) . '</pre>';
// echo '<pre>' . $json_response->result->croppings[0]->x1 . '</pre>';

$x1 = $json_response->result->croppings[0]->x1;
$y1 = $json_response->result->croppings[0]->y1;
$x2 = $json_response->result->croppings[0]->x2;
$y2 = $json_response->result->croppings[0]->y2;

$width = $x2 - $x1;
$height = $y2 - $y1;
$target_w = $json_response->result->croppings[0]->target_width;
$target_h = $json_response->result->croppings[0]->target_height;

// https://stackoverflow.com/questions/10233577/create-image-from-url-any-file-type
$image = imagecreatefromstring(file_get_contents($image_url));

// echo $x1 . " " . $y1 . " " . $x2 . " " . $y2 . " " . $width . " " . $height . " " . get_resource_type($image);

$imageCropped = imagecrop($image, ['x' => $x1, 'y' => $y1, 'width' => $width, 'height' => $height]);

if ($imageCropped !== FALSE) {
    header('Content-Type: image/png');
    imagepng($imageCropped, 'image_cropped.png');
    header("Location: ./image_cropped.png");
    imagedestroy($imageCropped);
}
imagedestroy($image);
?>