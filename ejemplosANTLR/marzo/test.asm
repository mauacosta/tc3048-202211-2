
    .text
main:




    li      $a0                1

    sw      $a0    0($sp)
    addiu   $sp    $sp        -4

    li      $a0                2

    lw      $t1    4($sp)
    add     $a0    $a0        $t1
    addiu   $sp    $sp        4

    sw      $a0    0($sp)
    addiu   $sp    $sp        -4

    li      $a0                3

    lw      $t1    4($sp)
    add     $a0    $a0        $t1
    addiu   $sp    $sp        4

    sw      $a0    0($sp)
    addiu   $sp    $sp        -4

    li      $a0                4

    lw      $t1    4($sp)
    add     $a0    $a0        $t1
    addiu   $sp    $sp        4

    li	$v0     10		                        #10 para cerrar
    syscall			                            #cerrar
