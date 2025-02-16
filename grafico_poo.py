# grafico_poo.py
import matplotlib.pyplot as plt
meses=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
vendas=[1500,1727,1350,1775,1052,1200,1300,1200,1100,1400,1500,1800]
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.title('Vendas por mês')
barra=plt.bar(meses,vendas,color='darkblue',fontweight='bold')
plt.bar_label(barra)
plt.yticks([])
plt.box(False)
plt.show()
