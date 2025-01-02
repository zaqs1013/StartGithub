<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>회원 관리 시스템</title>
</head>
<body>
    <h1>로그인 확인</h1>
    
    <?php
    //앞에서 넘겨온 값 받기
    $id = $_POST['id'];
    $pw = $_POST['pw']; 

    session_start(); //세션 시작

    //DB접속
    $dbcon = mysqli_connect('localhost', 'root', '', 'kt'); //데이터베이스 접속
    //질의 전달
    
    $query = "SELECT * FROM dbphp WHERE id = '$id'";
    $result = mysqli_query($dbcon, $query); //쿼리 전송

    $row = mysqli_fetch_assoc($result); //mysqli_query 를 통해 얻은 리절트 셋(result set)에서 
    //레코드를 1개씩 리턴해주는 함수

    if ($row) { //조건문 row에서
        if ($pw == $row['pw']) { //입력받은 값과 데이터 베이스의 pw가 같은지 확인.
            $_SESSION['userid'] = $row['id']; //데이터베이스의 ID가 같은지 확인
            $_SESSION['time'] = time(); //세션 부여
            echo "<script>alert('로그인 성공!'); location.replace('./test_01.php');</script>";
        } else {
            echo "<script>alert('비밀번호가 올바르지 않습니다!');
            location.replace('./rogin.php');</script>";
        }
    } else {
        echo "<script>alert('비밀번호가 올바르지 않습니다!');
        location.replace('./rogin.php');</script>";
    }

    mysqli_close($dbcon);
    ?>

    <a href="./rogin.php">뒤로가기</a>
</body>
</html>
