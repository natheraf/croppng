<?php

$uploadType = $_POST['uploadType']; // singleUpload zipUpload
$apiType = $_POST['apiType']; // cloudinaryAPI imaggaAPI
$croppedWidth = $_POST['croppedWidth'];
$croppedHeight = $_POST['croppedHeight'];

if ($croppedWidth == '') {
    $croppedWidth = 500;
}
if ($croppedHeight == '') {
    $croppedHeight = 500;
}

if ($uploadType == "singleUpload") {
    echo 'Type of upload recieved: Single Image upload<br>';

    $imageURL = $_POST['imgURL'];

    if ($imageURL == '') {
        
        // only cloudinaryAPI has a 10MB limit, but we set it for both anyways
        if ($_FILES['fileUpload']['size'] / 1048576 > 10) {
            die('Uploaded file too large. Only 10MB or less');
        }

        echo 'No Image URL found, checking uploaded image...<br>';
        if ($_FILES['fileUpload']['error'] !== UPLOAD_ERR_OK) {
            die('Error: No file uploaded or upload failed');
        }
        echo 'Uploaded File found! <br>Checking if file is image...<br>';
        
        $info = getimagesize($_FILES['fileUpload']['tmp_name']);
        if ($info === FALSE) {
            die("Unable to determine image type of uploaded file");
        }
        echo 'Image type found! <br>Checking if image is JPEG or PNG...<br>';

        if (($info[2] !== IMAGETYPE_JPEG) && ($info[2] !== IMAGETYPE_PNG)) {
            die("Not a JPEG/PNG");
        }
        $imgType = '.jpg';
        if ($info[2] === IMAGETYPE_PNG) {
            $imgType = '.png';
        }

        echo 'Image successfully validated!';
        move_uploaded_file($_FILES['fileUpload']['tmp_name'], './original_img' . $imgType);
    } else {
        echo 'Image URL found!<br>';
    }
} else if ($uploadType == "zipUpload") {
    echo 'Type of upload recieved: Zip file upload<br>';
} else {
    echo 'upload type not found';
    die();
}

echo '<h3>Original Image<h3><br>';
if ($imageURL == '') {
    echo '<img src="' . './original_img' . $imgType . '" alt="original_image"><br>';
} else {
    echo '<img src="' . $imageURL . '" alt="original_image"><br>';
}
echo '<h3>Cropped Image<h3><br>';
if ($apiType == "cloudinaryAPI") {
    include "./cloudinaryAPI.php";
    echo $imgtag;
} else {
    include "./imaggaAPI.php";
}
?>