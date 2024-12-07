<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>웹 프로그래밍</title>
</head>
<body>
    <?php
    $age = $_POST['age'];
    $num = $_POST['num'];
    $time = $_POST['time'];

    switch($age){
        case 1:
            $money = 20000;
            $type = "대인";
            break;
        case 2:
            $money = 15000;
            $type = "청소년";
            break;
        case 3:
            $money = 0;
            $type = "유아";
            break;
    }

    $fmoney = $money * $num;

    if($time == 't3'){
        $fmoney = $fmoney - ($fmoney * 0.2);
        echo "입장 인원은 $num 명이며,  $type 입니다. 총 지불 금액은" .number_format($fmoney). "원입니다.
        <br>야간시간대로 20%할인되었습니다.";
        
    }else{
        echo "입장 인원은 $num 명이며,  $type 입니다. 총 지불 금액은" .number_format($fmoney). "원입니다.";
    }
    
    ?>

</body>
</html>
