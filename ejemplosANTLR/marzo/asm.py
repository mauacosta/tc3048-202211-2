from string import Template

tpl_start = """
    .text
main:
"""

tpl_end = """
    li	$v0     10		                        #10 para cerrar
    syscall			                            #cerrar
"""

tpl_immediate = Template("""
    li      $$a0                $immediate
""")

tpl_suma = Template("""
$left
    sw      $$a0    0($$sp)
    addiu   $$sp    $$sp        -4
$right
    lw      $$t1    4($$sp)
    add     $$a0    $$a0        $$t1
    addiu   $$sp    $$sp        4
""")

tpl_printint = """
	li	    $v0     1               #para imprimir enteros
	syscall			                #imprimir
"""

"""
	i: .word 0
    

	li 	$v0, 5  			# syscall to read int
	syscall					# leer int
    move	$t0,$v0         # resultado queda en $v0

    la	$t1, array	#cargar la direccion de array a $t1

.data
msg: .asciiz “\nHello, World!\n”

li $v0, 4
la $a0, msg
syscall
"""