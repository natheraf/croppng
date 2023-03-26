<?php
if(isset($_FILES['file'])) {
  $file_name = $_FILES['file']['name'];
  $file_size = $_FILES['file']['size'];
  $file_tmp = $_FILES['file']['tmp_name'];
  $file_type = $_FILES['file']['type'];
  $file_ext = strtolower(end(explode('.', $_FILES['file']['name'])));
  
  // Validate the file type and size
  $valid_extensions = array('jpeg', 'jpg', 'png');
  $max_size = 10 * 1024 * 1024; // 10MB
  if(!in_array($file_ext, $valid_extensions)) {
    echo "Error: File type not allowed.";
    exit();
  }
  if($file_size > $max_size) {
    echo "Error: File size too large.";
    exit();
  }
  
  // Upload the file
  $upload_path = "uploads/";
  $upload_file = $upload_path . basename($file_name);
  if(move_uploaded_file($file_tmp, $upload_file)) {
    // Display the uploaded image to the user
    echo '<img src="' . $upload_file . '" />';
  } else {
    echo "Error: Failed to upload file.";
  }
}
?>
