4️⃣ CBV vs FBV:

. Na sua visão, quais vantagens você percebe ao usar CBV no lugar de FBV?

Class-Based Views são mais robustos e mais vantajosos para manutenção de sistemas extensos onde muita repetição pode acontecer. 

. Quando você usaria uma CBV? Quando manteria uma FBV?

CBVs são bons para evitar reutilização de códigos e para sobrescrever parte do comportamento de um código.
FBVs são simples e faceis de escrever e ler. Podem ser usados para lidar com detalhes específicos do código.

5️⃣ Templates:

.Por que é importante separar a lógica de negócio (views) da camada de apresentação (templates)?

Organização, manutenção e reutilização do código, separando lógica de HTML para melhor leitura e o mesmo template pode ser usado para diversas funções sem precisar ser duplicado.

.Qual o impacto disso na manutenção e evolução de uma aplicação?

Evita escrita manual de valores, o que pode causar erros.
Podemos reutilizar e extender o html para outras partes e funções do site, como formulários.

6️⃣ Models e qualidade de software:

.Por que um design de dados bem pensado (Models bem modelados) é fundamental para a qualidade de uma aplicação?

Para manutenção e manipulação de dados com eficiencia e de facil manutenção, além de garantir que os dados fiquem seguros e que possam ser extendidos com facilidade.

.Quais riscos você vê em um projeto onde os Models não são bem estruturados?

Dificuldades para modificar e de manutenção, possivelmente perda de performance ou de dados e podem criar obstáculos para a expansão do código.