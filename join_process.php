<!DOCTYPE html>
<html>
    <head>
    <meta charset = 'utf-8'>
    <title>회원 관리 시스템</title>
    </head>
<body>

    <h1>회원 가입</h1>

    <?php
    $id = $_POST['id'];
    $pw = $_POST['pw'];
    $phone = $_POST['phone'];
    
    $dir = './image/';
    $filename = basename($_FILES['uphoto']['name']);
    $imagepath = $dir.$filename;

    move_uploaded_file($_FILES['uphoto']['tmp_name'], $imagepath);  
    //DB 연결과 선택
    $dbcon = mysqli_connect('localhost','root','');
    mysqli_select_db($dbcon, 'kt');
    
    //질의전송
    $qurry = "insert into dbphp values(null, '$id','$pw','$phone','$imagepath')";
    $result = mysqli_query($dbcon, $qurry);
    
    if($result){
        echo "$id 님의 정보가 잘 입력되었습니다. 회원가입 완료!";
    }else{
        echo "알 수 없는 오류가 발생하여 가입 실패하였습니다.";
    }
    
    //연결해제
    mysqli_close($dbcon);
    ?>

    <a href = './join.php'>뒤로가기 </a>

</body>
</html>