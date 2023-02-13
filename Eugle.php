<?php

function isEugle()
{
    $g = [[0,1,6,0],[0,0,9,1],[7,7,6,7],[1,0,0,0]];
    $h = [];
    $e = [];
    $idk = 0;
    foreach ($g as $i) {
        $h[] = array_sum($i);
    }
    foreach ($h as $j) {
        $e[] = $j % 2;
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

echo isEugle();

?>
