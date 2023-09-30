# ADA1011-Projeto de Extração de Dados I
Grupo:
[Celice Lopes](https://github.com/celicelopes)
[Caio Uehara](https://github.com/caiouehara)
[Eric de Carvalho](https://github.com/EricRdC)
[Caroline Brum]()
[Isaac]()

## Sistema de Monitoramento de Avanços no Campo da Genômica

### Contexto:

O grupo trabalha no time de engenharia de dados na HealthGen, uma empresa especializada em genômica e pesquisa de medicina personalizada. A genômica é o estudo do conjunto completo de genes de um organismo, desempenha um papel fundamental na medicina personalizada e na pesquisa biomédica. Permite a análise do DNA para identificar variantes genéticas e mutações associadas a doenças e facilita a personalização de tratamentos com base nas características genéticas individuais dos pacientes.

A empresa precisa se manter atualizada sobre os avanços mais recentes na genômica, identificar oportunidades para pesquisa e desenvolvimento de tratamentos personalizados e acompanhar as tendências em genômica que podem influenciar estratégias de pesquisa e desenvolvimento. Pensando nisso, o time de dados apresentou uma proposta de desenvolvimento de um sistema que coleta, analisa e apresenta as últimas notícias relacionadas à genômica e à medicina personalizada, e também estuda o avanço do campo nos últimos anos.

O time de engenharia de dados tem como objetivo desenvolver e garantir um pipeline de dados confiável e estável. As principais atividades são:

1. Consumo de dados com a News API:
Implementar um mecanismo para consumir dados de notícias de fontes confiáveis e especializadas em genômica e medicina personalizada, a partir da News API:
https://newsapi.org/

2. Definir Critérios de Relevância:
Desenvolver critérios precisos de relevância para filtrar as notícias. Por exemplo, o time pode se concentrar em notícias que mencionem avanços em sequenciamento de DNA, terapias genéticas personalizadas ou descobertas relacionadas a doenças genéticas específicas.
3. Cargas em Batches:
Armazenar as notícias relevantes em um formato estruturado e facilmente acessível para consultas e análises posteriores. Essa carga deve acontecer 1 vez por hora. Se as notícias extraídas já tiverem sidos armazenadas na carga anterior, o processo deve ignorar e não armazenar as notícias novamente, os dados carregados não podem ficar duplicados.

![img1][img1]

4. Dados transformados para consulta do público final
A partir dos dados carregados, aplicar as seguintes transformações e armazenar o resultado final para a consulta do público final:
4.1 - Quantidade de notícias por ano, mês e dia de publicação;
4.2 - Quantidade de notícias por fonte e autor;
4.3 - Quantidade de aparições de 3 palavras chaves por ano, mês e dia de publicação (as 3 palavras chaves serão as mesmas usadas para fazer os filtros de relevância do item 2 (2. Definir Critérios de Relevância)).
Atualizar os dados transformados 1 vez por dia.

![img2][img2]

Além das atividades principais, existe a necessidade de busca de dados por eventos em tempo real quando é necessário, para isso foi desenhado duas opções:


Opção 2 - Webhooks com notificações por eventos:
Configurar um webhook para adquirir as últimas notícias a partir de um evento representado por uma requisição POST e fazer a chamada da API e por fim armazenar os resultados temporariamente. Em um processo paralelo, verificar os resultados armazenados temporiamente e armazenar no mesmo destino do item 3 (3. Cargas em Batches) aqueles resultados que ainda não foram armazenados no destino (os dados carregados não podem ficar duplicados). E por fim, eliminar os dados temporários após a verificação e a eventual carga.

![img3][img3]

Atividades que precisam ser realizadas pelo grupo definido em aula.

O grupo precisa construir o pipeline de dados seguindo os requisitos das atividades principais e escolher entre a Opção 1 e Opção 2 para desenvolvimento.


[img1]:"https://doc-00-3k-docs.googleusercontent.com/docs/securesc/mq6ug227f2l35jg4hc6c5oq0ir78lcmg/0i7ooen0k4uo54fgiesc1rpve23e16m2/1696088475000/07163535402014548785/09952603269530787624/1QLZBxgK4c4_yysUnvtamuwXzRJm4nNit?e=view&ax=AA75yW7rjJAH_M3_HP3Y14i5KOSJ3gv5TQuLA8s-9rM4MFurF7rSnNVUkUr5cEaHEDBWBtlT7ibDJU3EZ7i3D10Nxk0TdPFWpk7ULzzLX9AK_goVCaQHbQ2uE9TNmjMcFVZF7hGor_ukoveRr5opaSLlsHbP4k4Vzs2qpOricEnYSgY21upu9p2h7JUNf_8UKfskvpAIGRO175MWP0DZVGHozUdZEeuTgvYAU8Ra-tfHYEdZlUvcza5v9K8JwFFaDbbimAoOnYsBUtisU2V9407WL6Cp5SEewvhbpuIqrnezoziv-5F63h1D80NBdPqT2YOGiOfnUSnwFiCWgCZszaXsZ39CC-GkMSe5wjsEVbXwGYa8A6X-X5oVR7DKclyx8GHQfoZZ9_hVQvmgPQGpv8ykIkQqJvwKKiOKUyq5gho_uRDNkhZbrwdvEsz9eCu8tY5vu0QYmsHsDXneVhE7nskntMZ8ct12uBewPRc8sVJgkyvxtYemQTNLuLnRmuYOFFR8J18YT4Gsa8-LP9RWhwfq6Q7zRVBRwYm_sP8gj3TLiva7temOhVZjG0UAU8UJ71LV3sJNgNlU7xzAZVI-DS786GI6KKb6mn7JNiTnfhq63wLWV14uYASnbEaXm0fMd1kereeE6NQdLwQE5GtjFmZOhTpa9pn1WtM5CpCzWGoSksj-q1M7Bj_X59xxwueAkX0818G7obmIxlnelUNxxmc9X8VMg8wTM3m9MdIb1p-HQ_oJXYQAe18OeYGapavAh3eQqF6dOTM7MF0-Ki2yIdKrGe9W44ZUsQhN5Rk03YZEn29Lf8xot6BXU21TynZe3Ae55ecmx4ebaYZqN0M7scU3VewlcgXZcVJGv_MfSwS1-Yrya4VCj2ATDGRUjaVqEaKyiLkoKVOLRi2TYKH5wXIWotBz3t-5TnGXlTybJvk&uuid=1318e554-18d4-4b0b-8761-1080f80d14a2&authuser=0"
[img2]:"https://doc-04-3k-docs.googleusercontent.com/docs/securesc/mq6ug227f2l35jg4hc6c5oq0ir78lcmg/ip6ns6bpu47pmgrinv376gn9pg03uk4n/1696088475000/07163535402014548785/09952603269530787624/1QOFkzKrWqb-9CY3kC3_1XkTWNVNE05dd?e=view&ax=AA75yW7DdqmQa3x27LwtJ8id7wla8Vaj5x1_4Q434O9NsKRHADvPWfVZ9oDokqW-YKLBITy-ASkmVmRd6hofCkFEf1owPj8GAe8E4-OTaTwRjLPyJ4GO-dBRw-pIZxayYttec-rggtMDR8jpBmiJcgRUNgNV0SACHlg7oyhMKTfsRpfsT0Mvsh6XJ-B-p_cKAQuqPQHSD8xQ4OU4S9g9gYCIe_ic61qIWXcG1OU9gxxhTjHhrkZtXTBy1lwinSAwtYON18NKtkD8G5JzWtc2XGQLHnknFrGmoWGT3H5tpcu58QGudMCHgfVowAwlnh1cByZGVKZR6JLguNVI2luz3sZAqcbQiEiXXcGnNozcWPTkU8vp67peogPYtPpnekdh1zFzsEffQzgbGP57xkg9qphwpNEkyup_bLn-R3yH7WlzgvKY72ValynXnMmSUeD3Cfag7oOH0cxi-OkoM0G2crUrmhJPIDC-tO-hzatEJ3gQ2coB23XHMLuJDQK0agTZ9D1XWW5zZmM1X3xNuQlkR9MaHn-KGohbovDzjj2H42jJlODrw1kwIDpzshG93CuhdzK2qCKrgvSRUhLSQPaZYbcrCJAuIGI0BYrwEjBaADb6rVjYCfmyp-CPJjes4_KkVQqZCWDNjKUgSbGxNzogHU16xatbRNadcvi_nerhiz5Zk7R_OweJckOjSRz5RdBmIklRy-5rUmjHwnMQ233toxW3Y0dfFqJv0Mfto_EfREKKW03xMJIyqBm2BcBU-zAIYdsbIKp6RkZXnxrbPck9WIinzANHO5sH9qnFkUdX1gYU0KHsia42K2S7eSIap2BRRi1bsZZSqCxWRpIl4dcqLUTs-EayfhDdf90Mmpsd0P-X2S3iLHpJxiYhEHTvDHH3XAoFXQ4zdN2GcMFsgpinZJlFKJsvd0lN5BBgcYDbXoA&uuid=957671c9-e24d-4af4-a524-33af19aaf0a0&authuser=0"
[img3]:"https://doc-00-3k-docs.googleusercontent.com/docs/securesc/mq6ug227f2l35jg4hc6c5oq0ir78lcmg/es4in1omru8vjh718g3ba4dvef6c00ag/1696088400000/07163535402014548785/09952603269530787624/1Px6Jp3aNuF-wpn_9earonylEMebzOcBW?e=view&ax=AA75yW4ppax-MaSBTq-OrdEyQeG07GvXSFB5_BSD_7LkdL7KZlpMhZww_x2u5ob_Y8WAuojkH2f-VKTdXPRae6zXoRduz1ErO_Qc6eQtCn2I9aGEvmgZ3Nuzk9zLUeSB_K0t6B753FEF3GDlUIa7kM6NNaO7pQC06RxfiVUx0NeWKoWzKts4wdpFIk2LB3-RDoJHfw5lJMokUdW9C_6sRkzG5AGfeDP7AnF5djVD4h0dp25S3Y548Gf-3WYFwwg8zEWSOM0SwZR6IVDzcm7J5mmNqeKKmaGtHx5NfYDnvfoipGVnDDqq56XtMzLcGRbrYpaHk88hnMtgNAomqaYzkt6TrOqny1oRzv8awHlaDvAEuX7x2L8j7rqUEWTAcJd4UuY_4hvDGcamaU-fwYF3MOYDejWuq0mWCe5XORCBtXETiZm9nFhyTSC_7aF3upEUZ2XYq_A8Uo3sWTSncbnae5uxzRNkC6Zb6VOsJ8rDy2FIzzwwcD9EVvtutE66LcM7ByGVdA9nIMGSoQWVHugnbRe90q5e7CJCfGX4GTV73kHMEO_rbAe9B6JdrNC4IwvWrEcqnBEXsWjMfKteR6vNFEkdearcXFaYaxDjoVHbleR9kgQRRUc9NTTPeCEGEOR3LG_VoMaxm_IhdUL75xqPHXLKmEFI8idLwdgc4s5qpg8lPsq15jAAbGvyXiTYILWS2leLqVtl_cnJXY4oE9Qaku8rTbZRF6YDjJ4h6pOnmiJRdZ-EEcOSQdzmzWsHlxXHLBDisZ5ByAWtF4ss0DVWTW-c8vBsxgntEEXHiAgj-VjwOCN6ZwHyg5rhd8s_HgM9la_t1cCDXphnIv7QvvNoLvGEBvdncIlnawkZPRDFzPmJWnbQzxq8deKm_UQcw2CifdE3eRh1HsyNQRBTYPx2kOMOOMdYdE9johglzeWOqx8&uuid=c8f27802-3e61-4d0a-ace3-437ea8f1008f&authuser=0&nonce=oq27dnpnmq8oo&user=09952603269530787624&hash=smohgg8rino8td1cbauhiofppdqs7t4m"