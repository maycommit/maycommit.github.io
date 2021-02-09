---
layout: post
title:  "Começando com TLA+"
date:   2021-02-08
comments: true
categories: tla+
---

Recentemente iniciei meus estudos sobre a especificação formal de algoritmos utilizando TLA+. Estou criando essa nota para organizar meu modo de pensar e ajudar outras pessoas que estão interessadas nesta area.

## Especificação formal

Sistemas de software ou hardware bem elaborados ainda podem conter erros sutis capazes de gerar perdas catastróficas dependendo da situação. Por isso a engenharia de software oferece mecanismos que permitem a construção de sistemas mais confiáveis, como os métodos formais que são um conjunto de técnicas  baseadas em formalismos matemáticos para a especificação e verificação de sistemas de hardware e software. {% cite 10.1145/242223.242257 %}
 
Especificar um algoritmo formalmente significa descrevê-lo de forma abstrata, completa e precisa utilizando uma linguagem com sintaxe e semântica formalmente definidas {% cite 10.5555/1841764 %}. Em outras palavras, uma especificação formal descreve o que o algoritmo deve fazer e não como fazer, utilizando uma linguagem que faz o uso de formalismos matemáticos como teoria dos conjuntos, lógica etc...

## Linguagem TLA+
TLA+ é uma linguagem formal de especificação desenvolvida por Leslie Lamport...


---
{: data-content="references"}
{% bibliography --cited_in_order %}