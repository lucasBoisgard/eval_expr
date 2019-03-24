import operator

def get_operator (op) :
	return {
		'+' : operator.add,
		'-' : operator.sub,
		'*' : operator.mul,
		'/' : operator.div,
		'%' : operator.mod,
	}[op]

def eval_helper (expr1, expr2, sign = "+") :
	return get_operator(sign)(int(expr1), int(expr2))

def eval_expr (nb) :
	i, expr1, expr2 = 0

	while '(' in nb or ')' in nb :
		if nb[i] == '(' or nb[i] == ')' :
			nb = nb[0:i] + '' + nb[i+1:]
		i = i + 1
	return int(nb)
	# while nb[i] != ")" :

# print eval_expr("(3+2)*5")
print eval_helper("2", "3", "+")