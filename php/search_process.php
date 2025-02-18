<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>
        웹프로그래밍
    </title>
</head>
<body>
    <?php
    $name = $_POST['name'];
    $gender = $_POST['gender'];

    if ($gender === 'option1') {
        $query = "SELECT * FROM member;";
    } else if ($gender === 'option2') {
        $query = "SELECT * FROM member WHERE gender = 'male';";
    } else if ($gender === 'option3') {
        $query = "SELECT * FROM member WHERE gender = 'female';";
    } else {
        die("<p>잘못된 옵션이 선택되었습니다.</p>"); // 유효하지 않은 옵션 처리
    }
    
    
    //DB 연결과 선택
    $dbcon = mysqli_connect('localhost','root','');
    mysqli_select_db($dbcon, 'kt');
    
    //질의전송

    $result = mysqli_query($dbcon, $query);
    $row = mysqli_fetch_array($result);

    echo "{$name} 님이 검색하셨습니다.<br><br>";
    if($result){
        while ($row = mysqli_fetch_assoc($result)) {           
            echo "이름: {$row['uname']}, 나이: {$row['uage']}, 성별: {$row['gender']}, 생년월일: {$row['birth']}<br>";
        }
    }else{
        echo "알 수 없는 오류가 발생하여 가입 실패하였습니다.";
    }
    
    //연결해제
    mysqli_close($dbcon);
    ?>

    <a href = './search.php'>뒤로가기 </a>
</body>
</html>