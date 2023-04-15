<?php
// https://stackoverflow.com/questions/34264121/why-i-am-getting-fatal-error-uncaught-exception-guzzlehttp-exception-requestex
// https://stackoverflow.com/questions/35638497/curl-error-60-ssl-certificate-prblm-unable-to-get-local-issuer-certificate
// https://stackoverflow.com/questions/29822686/curl-error-60-ssl-certificate-unable-to-get-local-issuer-certificate/34883260#34883260

// https://cloudinary.com/documentation/resizing_and_cropping
// https://console.cloudinary.com/console/c-ebdb8253630444a271b801e04cc695

require_once(__DIR__ . '../../vendor/autoload.php');

use Cloudinary\Cloudinary;

// $cloudinary = new Cloudinary(
//     [
//         'cloud' => [
//             'cloud_name' => 'durd8kb5e',
//             'api_key'    => '215961418216461',
//             'api_secret' => '6AOiayvtgYxKvBUsru5R6Hqw1_U',
//         ],
//     ]
// );
// Configuration::instance('cloudinary://my_key:my_secret@my_cloud_name?secure=true');

// Use the Configuration class 
use Cloudinary\Configuration\Configuration;
Configuration::instance('cloudinary://215961418216461:6AOiayvtgYxKvBUsru5R6Hqw1_U@durd8kb5e?secure=true');

// Use the UploadApi class for uploading assets
use Cloudinary\Api\Upload\UploadApi;

// Use the Resize transformation group and the ImageTag class
use Cloudinary\Transformation\Resize;
use Cloudinary\Transformation\Background;
use Cloudinary\Transformation\Gravity;
use Cloudinary\Tag\ImageTag;

// Create the image tag with the transformed image
$imgtag = (new ImageTag('cld-sample-3'))
->resize(Resize::fill()->width(200)
->height(300)
->gravity(
Gravity::autoGravity())
);

echo $imgtag;

?>