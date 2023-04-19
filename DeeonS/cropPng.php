<?php


$uploadType = $_POST['upload']; // singleUpload zipUpload
$apiType = $_POST['apiType']; // cloudinaryAPI imaggaAPI
$croppedWidth = $_POST['croppedWidth'];
$croppedHeight = $_POST['croppedHeight'];

if ($croppedWidth == '') {
    $croppedWidth = 500;
}
if ($croppedHeight == '') {
    $croppedHeight = 500;
}
if($uploadType == "upload"){
    echo 'Type of upload recieved: Single Image upload';

    if($uploadType == ''){
        echo 'No Image found';
        if ($_FILES['fileUpload']['error'][0] !== UPLOAD_ERR_OK) {
            die('Error: No file uploaded or upload failed');
        }
        echo 'Uploaded File found! <br>Checking if file is image...<br>';

        $info = getimagesize($_FILES['fileUpload']['tmp_name'][0]);
        if ($info === FALSE) {
            die("Unable to determine image type of uploaded file");
        }
         echo 'Image type found! <br>Checking if image is JPEG or PNG...<br>';
         if (($info[2] !== IMAGETYPE_JPEG) && ($info[2] !== IMAGETYPE_PNG)) {
            die("Not a JPEG/PNG");
        }else {
        echo 'Image URL found!<br>';

        echo '<h3>Original Image<h3><br>';
        echo '<img src="' . $uploadType . '" alt="original_image"><br>';
        echo '<h3>Cropped Image<h3><br>';
        if ($apiType == "cloudinaryAPI") {
            include "./cloudinaryAPI.php";
            echo $imgtag;
        } else {
            include "./imaggaAPI.php";
        }
    }
}else {
    echo 'upload type not found';
}
?>