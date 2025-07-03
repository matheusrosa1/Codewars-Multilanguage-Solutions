<?php

function booleanToString($b) {
    // Verifica se o valor é booleano e retorna a string correspondente
    if (is_bool($b)) {
        return $b ? 'true' : 'false';
    }
    // Se não for booleano, retorna uma string vazia
    return '';
}