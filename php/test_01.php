<!DOCTYPE html>
<html lang="ko">
<head>
        <meta charset="utf-8">
        <title>회원가입 페이지</title>
        <link rel="stylesheet" href="./style1.css">
    </head>
<body>

<?php
 session_start(); 
 if(isset($_SESSION['id'])){
 $userid = $_SESSION['id'];
 echo "Welcome!";
 }else{
 echo "Access denied";
 }
?>
<p style="border:1px solid red; backgrount-color: skyblue;">
안녕하세요!
</p>
</body>
</html>
