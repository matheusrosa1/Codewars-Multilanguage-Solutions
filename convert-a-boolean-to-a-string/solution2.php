<?php

function booleanToString($b)
{
  if (is_bool($b)) {
    return $b ? 'true' : 'false';
  }
  return '';
}
