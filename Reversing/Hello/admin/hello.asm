section .data
	text1 db "cyberQuest{", 10
	greet db "Hello, World!", 10
	text2 db "H1_", 10
	text4 db "0u_", 10
	text8 db "f696350da0", 10
	text5 db "t0d", 10
	text6 db "4y_", 10
	text9 db "b4b0cc0a49", 10
	text7 db "8f7044571ec", 10
	text3 db "H0w_ar3_y", 10
	text10 db "3}", 10

section .text
	global _start

_start:
	mov rax, 1
	mov rsi, 1
	mov rsi, greet
	mov rdx, 14
	syscall

	mov rax, 60
	mov rsi, 0
	syscall
