<?php
ini_set('xdebug.var_display_max_depth', '10');
ini_set('xdebug.var_display_max_children', '256');
ini_set('xdebug.var_display_max_data', '1024');

$sizes = array(
    $croppedWidth . 'x' . $croppedHeight
);

$api_credentials = array(
    'key' => 'acc_3484679611ff3db',
    'secret' => 'ba0a95b2d3e3b155664a5609013f5cec'
);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://api.imagga.com/v2/croppings?image_url=' . urlencode($imageURL) . '&resolution=' . implode(',', $sizes));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($ch, CURLOPT_HEADER, FALSE);
curl_setopt($ch, CURLOPT_USERPWD, $api_credentials['key'].':'.$api_credentials['secret']);

$response = curl_exec($ch);
curl_close($ch);

$json_response = json_decode($response);
// var_dump($json_response);

$x1 = $json_response->result->croppings[0]->x1;
$y1 = $json_response->result->croppings[0]->y1;
$x2 = $json_response->result->croppings[0]->x2;
$y2 = $json_response->result->croppings[0]->y2;

$width = $x2 - $x1;
$height = $y2 - $y1;
$target_w = $json_response->result->croppings[0]->target_width;
$target_h = $json_response->result->croppings[0]->target_height;

$image = imagecreatefromstring(file_get_contents($imageURL));

$imageCropped = imagecrop($image, ['x' => $x1, 'y' => $y1, 'width' => $width, 'height' => $height]);

if ($imageCropped !== FALSE) {
    imagepng($imageCropped, 'image_cropped.png');
    echo '<img src="./image_cropped.png" alt="image_cropped.png" width="' . $croppedWidth . '" height="' . $croppedHeight . '">';
    // header("Location: ./image_cropped.png");
    imagedestroy($imageCropped);
}
imagedestroy($image);
?>