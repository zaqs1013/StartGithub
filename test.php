<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>웹 프로그래밍</title>
</head>
<body>
    <?php

    $key = $_POST['key'];
    $mo = $_POST['mo'];

    $result = ($key - 100) * 0.9;
    
    if($result < $mo){
        echo "다이어트 필요함";
    }else{
        echo "다이어트 불필요";
    }

    ?>

</body>
</html>
