<?php

function isEugle($g) {
    $h = array();
    $e = array();
    $idk = 0;
    foreach ($g as $i) {
        array_push($h, array_sum($i));
    }
    foreach ($h as $j) {
        array_push($e, $j % 2);
    }
    foreach ($e as $k) {
        if ($k == 1) {
            $idk += 1;
            if ($idk == 3) {
                return false;
            }
        }
    }
    return true;
}

echo "Enter nums: \n";
$g = array();
while (true) {
    $row = trim(fgets(STDIN));
    if ($row == ".") {
        break;
    }
    $row_nums = explode(",", $row);
    foreach ($row_nums as $num) {
        if (!is_numeric($num)) {
            echo "Please enter integers only\n";
            exit();
        }
    }
    array_push($g, $row_nums);
}

echo "It is Eugle: " . var_export(isEugle($g), true) . "\n";

?>
