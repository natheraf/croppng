<?php
require_once(__DIR__ . '../../vendor/autoload.php');

use Cloudinary\Cloudinary;
// Use the Configuration class 
use Cloudinary\Configuration\Configuration;
// Use the UploadApi class for uploading assets
use Cloudinary\Api\Upload\UploadApi;
// Use the Resize transformation group and the ImageTag class
use Cloudinary\Transformation\Resize;
use Cloudinary\Transformation\Background;
use Cloudinary\Transformation\Gravity;
use Cloudinary\Tag\ImageTag;

$cloudinary = new Cloudinary(
    [
        'cloud' => [
            'cloud_name' => 'durd8kb5e',
            'api_key'    => '215961418216461',
            'api_secret' => '6AOiayvtgYxKvBUsru5R6Hqw1_U',
        ],
    ]
);
Configuration::instance('cloudinary://215961418216461:6AOiayvtgYxKvBUsru5R6Hqw1_U@durd8kb5e?secure=true');

if ($imageURL == '') {
    $result = $cloudinary->uploadApi()
    ->upload('./original_img' . $imgType);
} else {
    $result = $cloudinary->uploadApi()->upload($imageURL, [
        "folder" => "CropPNG/imgs"
    ]);
}

// Create the image tag with the transformed image
$imgtag = (new ImageTag($result['public_id']))
->resize(Resize::fill()->width($croppedWidth)
->height($croppedHeight)
->gravity(
Gravity::autoGravity())
);

?>