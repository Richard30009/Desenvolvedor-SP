
sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
ot = float(19849.53)

total = float(sp + rj + mg + es + ot)
print(total)

spfinal = ((sp/total)*100)
rjfinal = ((rj/total)*100)
mgfinal = ((mg/total)*100)
esfinal = ((es/total)*100)
otfinal = ((ot/total)*100)

print('Porcentagem de SP aproximadamente {:.2f}'.format(spfinal))
print('Porcentagem de RJ aproximadamente {:.2f}'.format(rjfinal))
print('Porcentagem de MG aproximadamente {:.2f}'.format(mgfinal))
print('Porcentagem de ES aproximadamente {:.2f}'.format(esfinal))
print('Porcentagem de OUT aproximadamente {:.2f}'.format(otfinal))

