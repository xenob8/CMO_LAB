# CMO_LAB
<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 3

Conversion time: 2.202 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β33
* Mon Nov 28 2022 12:55:57 GMT-0800 (PST)
* Source doc: отчет архитектура ВС
* Tables are currently converted to HTML tables.
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!


WARNING:
You have 10 H1 headings. You may want to use the "H1 -> H2" option to demote all headings by one level.

----->



<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 3.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


# Постановка задачи


    Целью курсовой работы является создание модели вычислительной системы (ВС) или ее части на некотором уровне детализации, описывающей и имитирующей ее структуру и функциональность.


    Каждый реальный объект (реальная ВС) обладает бесконечной сложностью, множеством характеристик, внутренних и внешних связей. Модель есть приближенное описание объекта с целью получения требуемых результатов с определенной точностью и достоверностью.


    При необходимости исследования поведенческих характеристик ВС в процессе исследования выгодно использовать не сам объект, а его модель. Степень приближения модели к описываемому объекту может быть различной и зависит от требований задачи.


        Существуют различные типы моделей:


         Аналитические (математические) модели


         Аналоговые модели


         Физические модели


         Имитационные модели


        Последний тип моделей является предметом нашего изучения.


        Одним из подходов к построению имитационной модели


    является построение ее в виде системы массового обслуживания (СМО), с характерной для СМО терминологией: источник, буфер, прибор, диспетчер, заявка (требование).


# Описание СМО


## Источники:

**ИБ **- бесконечный источник

**ИЗ1 **- закон распределения: пуассоновский	для	бесконечных,


## Приборы:

**ПЗ2 **- прибор с законом распределения: пуассоновский	для	бесконечных,


## Дисциплины (диспетчеры):



* Буферизации
    * **Д10З2 **- диспетчер буферизации в порядке поступления
* Отказа
    * **Д10О5 **- диспетчер отказа
* Дисциплина постановки на обслуживание
    * выбор заявки из буфера
        * **Д2Б5 **- выбор заявки из буфера приоритет по номеру источника заявки в пакете
    * выбор прибора
        * **Д2П1 **- выбор прибора (приоритет по номеру прибора)


## Виды отображения результатов работы программной модели 


    Отражение результатов после сбора статистики(автоматический режим)

		**ОР1 **- сводная таблица результатов

Динамическое отражение результатов (пошаговый режим)	

		**ОД2 **- отображение динамики функционирования модели: формализованная схема модели, текущее состояние;


# Формализованная схема ВС



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](https://i.postimg.cc/RhMDmfnp/2.png)


Здесь Иi (i= 1..n) – источник заявок, который генерирует заявки, а все вместе n источников создают входной поток заявок в систему.

 

Каждая заявка приходит в СМО со своими характеристиками. Это T<sub>вх</sub> — время генерации заявки (время поступления её в СМО) и

номер заявки составленный из номера источника, сгенерировавшего заявку, и порядкового номера заявки от этого источника. Например, (2.3) – третья заявка от второго источника.

 

П   — приборы, которые обслуживают заявки и создают выходной поток заявок после обслуживания.

 

БП — буферная память (место для хранения очереди заявок).

 

В общей памяти хранятся заявки от различных источников. Порядок их записи в БП определяется только дисциплиной буферизации.

 

ДП — диспетчер постановки заявок. ДВ — диспетчер выбора заявок


## 
    Дисциплины буфферизации


### 
    Д1032 - В порядке поступления

Если в момент поступления заявок в систему все приборы оказываются занятыми, заявка последовательно занимает места в буфере памяти, начиная с первого. В случае освобождения какого-либо места в БП(буферная память) с номером N (заявка уходит на обслуживание или получает отказ), все заявки, стоящие на местах, начиная с (N+1), сдвигаются на одно место. Следующая заявка, вынужденная встать в очередь, всегда будет ставиться в ее конец, пока есть свободные места.


## Дисциплины отказа

Заявки могут получить отказ в обслуживании только в том случае, если к моменту прихода в систему очередной заявки все приборы и все места в буферной памяти окажутся занятыми. Тогда пришедшая заявка может либо сама уйти из системы (получить отказ), либо она имеет право занять место одной из заявок, стоящих в буферной памяти (выбить заявку из БП). &lt;Права> и &lt;возможности> этих заявок определяют дисциплины отказа.


### Д10О5

Заявка, сгенерированная источником и не нашедшая свободного места в буфере, уходит из системы, не изменяя состояния буфера. При этом она обязательно учитывается при подсчете общего количества сгенерированных источником заявок.


## Дисциплина постановки на обслуживание


### Д2Б5 — приоритет по номеру источника, заявки в пакете;

Освобождение прибора или его простой означает, что прибор готов взять заявку на обслуживание. Если в буфере есть очередь, то заявка поступает на прибор в момент его освобождения. Какую заявку поставить на обслуживание на освободившийся прибор определяют дисциплины выбора заявок.

Назовем  «пакетом»  совокупность  заявок  одного  источника, находящихся в буфере на момент освобождения одного из приборов. Количество  пакетов  в  БП  может  меняться  от  0  до  n,  где  n  — количество источников.

 

Когда при освобождении прибора происходит выбор первой заявки из буфера, вначале определяется самый приоритетный на данный момент пакет и происходит обслуживание заявок только этого пакета до тех пор, пока к моменту очередного освобождения прибора в БП не останется ни одной заявки этого пакета. Затем снова определяется самый приоритетный на данный момент пакет и далее повторяется весь процесс обслуживания этого пакета. Таким образом, происходит динамическая смена приоритетов обслуживания заявок, причем приоритетность пакетов можно регулировать, изменяя интенсивность генерации заявок источниками.


## **Дисциплины выбора прибора.**


### Д2П1 приоритет по номеру прибора.

Приоритеты приборов, также как и приоритеты источников определяются номерами приборов. Поэтому поиск свободного прибора ведется последовательным перебором, каждый раз начиная с самого приоритетного.


# Waveform



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


[https://wavedrom.com/editor.html](https://wavedrom.com/editor.html)

{

  signal: [

    {name: 'И1', wave: '03040..20...30', data: ["1,1","1,2","1.3","1.4"]},	

    {name: 'И2', wave: '0.70..80.90...', data: ["2.1","2.2","2.3","2.4","2.5"]},

    {name: 'И3', wave: '0...560.......', data: ["3.1","3.2"]},

    {name: 'П1', wave: '03......8....6', data: ["1.1",2.2, 3.2],  node: '........b....l'},

    {name: 'П2', wave: '0.7.......9...', data: ["2.1","2.3"], node: '..........d'},

    {name: 'П3', wave: '0..4.......5..', data: ["1.2","3.1"], node: '...........f'},

    {name: 'Б1', wave: '0...5......6.3', data: ["3.1","3.2","1,4"], node: '..........e.kn'},

    {name: 'Б2', wave: '0....6.....030', data: ["3.2","1.4"], node: '...........h.m'},

    {name: 'Б3', wave: '0.....8.090...', data: ["2.2","2.3"], node: '........a.c'},

    {name: 'отк', wave: '0......20.....', data: ["1.3",""]},

  ],

    

  edge: [

    'a-~>b',

    'c-~>d',

    'e-~>f обслуживание пакета 3' ,

	'h-~>k',

    'k-~>l выбор по пакету',

    'm-~>n'

   ],

  

  foot:{

   text:'Figure 100',

   tock:0

  },

  

}


# Пример технической системы, удовлетворяющей формализованному описанию


<table>
  <tr>
   <td>Система
   </td>
   <td>Обслуживание пациентов в поликлинике
   </td>
  </tr>
  <tr>
   <td>Источники
   </td>
   <td>Тип болезни у пациента. Например, инфекционные, неинфекционные, здоровые
   </td>
  </tr>
  <tr>
   <td>Приборы
   </td>
   <td>Врачи-специалисты в кабинете, в среднем обслуживающие пациента за время t (взятие анализов)
   </td>
  </tr>
  <tr>
   <td>Буфер
   </td>
   <td>Количество сидячих мест возле кабинета
   </td>
  </tr>
  <tr>
   <td>Дисциплина постановки в буфер
   </td>
   <td>В порядке поступления
   </td>
  </tr>
  <tr>
   <td>Дисциплина выбора из буфера
   </td>
   <td>Приоритет по типу болезни последнего зашедшего, чтобы минимизировать контакт людей с различным типом болезни в кабинете. Если таких людей в очереди нет, то по приоритету типа болезни
   </td>
  </tr>
  <tr>
   <td>Дисциплина отказа
   </td>
   <td>Если нет свободных сидячих мест, пациент негодует и идет в другой кабинет
   </td>
  </tr>
  <tr>
   <td>Дисциплина постановки на обслуживания
   </td>
   <td>Приоритет по номеру врача (который ближе всего сидит)
   </td>
  </tr>
</table>



# Ограничения и требуемые характеристики:



1. Количество обслуживаемых заявок за год: 30 240

    (12 часов по 7 человек на 30 дней * 12 мес)

2. Количество докторов в кабинете не может быть больше 7
3. Вероятность отказа должна составлять не более 5 %.
4. Загрузка приборов более 70%.
5. Среднее время пребывания в очереди не должно превышать 5 минут.
6. Максимальное время пребывания в очереди, не должно превышать 20 минут.

 


# 
    Таблица компонентов системы.

 


<table>
  <tr>
   <td>
    Количество типов больных
   </td>
   <td>
    3, возможно расширение
   </td>
  </tr>
  <tr>
   <td>
    Размер заявки
   </td>
   <td>
    1 пациент
   </td>
  </tr>
  <tr>
   <td>
    Размер буфера
   </td>
   <td>
    Необходимо установить минимальное
   </td>
  </tr>
  <tr>
   <td>
    Количество приборов
   </td>
   <td>
    &lt;=7
   </td>
  </tr>
  <tr>
   <td>Скорость работы источников
   </td>
   <td>
    Время наблюдения Tn = 1 час = 3600 с
<p>

    Кол-во событий 
<p>

    Здоровые: 20, <em>λ = 1/180</em>
<p>

    инфицированный: 10, <em>λ = 1/360</em>
<p>

    неинфицированный: 15, <em>λ = 1//240</em>
   </td>
  </tr>
  <tr>
   <td>
    Скорость работы приборов
   </td>
   <td> Смотреть в таблице “стоимость компонентов системы”
   </td>
  </tr>
</table>


 


# Стоимость компонентов системы


<table>
  <tr>
   <td>Наименование
   </td>
   <td>Характеристики
   </td>
   <td>Цена
   </td>
  </tr>
  <tr>
   <td>Врач высшего класса
   </td>
   <td>Среднее время обслуживания 5 минут
   </td>
   <td>700р / час
   </td>
  </tr>
  <tr>
   <td>Врач среднего класса
   </td>
   <td>Среднее время обслуживания 6 минут
   </td>
   <td>500р / час
   </td>
  </tr>
  <tr>
   <td>Врач студент
   </td>
   <td>Среднее время обслуживания 8 минут
   </td>
   <td>300р / час
   </td>
  </tr>
  <tr>
   <td>Одноместный стул
   </td>
   <td>Дополнительное место к буферу
   </td>
   <td>1000 р
   </td>
  </tr>
</table>



# Документация на ПО


## Модульная структура


    Разработка производилась на языке Python 3.9 с использованием фреймворка flask для поднятия сервера. 


    Приложение использует объектно-ориентированную парадигму программирования и содержит набор классов:



* Класс Source– класс источника
* Класс Instrument– класс прибора
* Класс SourcesProcessor - класс для генерации заявок
* Классы диспетчеров, для обработки заявки
* Класс StatsCollector для сбора статистики
* Класс App, который есть наша СМО

    Программа содержит точку входа в файле main.py. В нем мы создаем объект класса App и запускаем. Класс App содержит в основных метода - update() : обработать одну заявку и run() обработать все заявки.


### 
    Отображение результатов в автоматическом режиме:


### 
    Отображение результатов в пошаговом режиме:



# Результаты работы имитационной модели


## Определение количества реализаций.


    Количество реализаций, необходимое для получения нужной точности при заданной доверительной вероятности, можно оценивать по формуле:


    

<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")



    По результатам работы программы получено, что в большинстве случаев для достижения заданной точности необходимо от 2000 до 6000 заявок. Однако, в случаях, когда p мало (&lt;0.05) для достижения точности в 10% может потребоваться существенно больше заявок (20000-30000).


## Анализ результатов, выводы и рекомендации по выбору конфигурации системы.

Начнём с минимально возможной конфигурации, когда в кабинете будет работать один врач-студент и в очереди будет располагаться один стул. 


<table>
  <tr>
   <td><strong>Тип источника </strong>
   </td>
   <td><strong>  кол-во заявок</strong>
   </td>
   <td><strong>  p отк</strong>
   </td>
   <td><strong>  Tпреб</strong>
   </td>
   <td><strong>  Tбуф</strong>
   </td>
   <td><strong>  Tобсл</strong>
   </td>
   <td><strong>  Дбуф</strong>
   </td>
   <td><strong>  Добсл</strong>
   </td>
  </tr>
  <tr>
   <td>Здоровые         
   </td>
   <td>1108
   </td>
   <td>   0.81
   </td>
   <td>  12.60
   </td>
   <td>  5.60
   </td>
   <td>   7.00
   </td>
   <td> 95.29
   </td>
   <td>   0.00
   </td>
  </tr>
  <tr>
   <td>Инфец.     
   </td>
   <td>537
   </td>
   <td>   0.81
   </td>
   <td>  12.64
   </td>
   <td>  5.64
   </td>
   <td>   7.00
   </td>
   <td> 96.82
   </td>
   <td>   0.00
   </td>
  </tr>
  <tr>
   <td>Неинфец         
   </td>
   <td>875
   </td>
   <td>   0.81
   </td>
   <td>  12.76
   </td>
   <td>  5.76
   </td>
   <td>   7.00
   </td>
   <td> 86.35
   </td>
   <td>   0.00
   </td>
  </tr>
</table>


Очевидно, что такая конфигурация нас не устраивает.

Посчитаем, кого из врачей лучше всего нанимать

Сколько клиентов пройдет через одного доктора за тысячу рублей?

Профи - 17,  студент - 25,  средний - 20

Поэтому, выгоднее всего платить студентам. 



1. Заполним весь кабинет студентами.

<table>
  <tr>
   <td>
<strong>Номер источника  </strong>
   </td>
   <td><strong>  кол-во заявок</strong>
   </td>
   <td><strong>  p отк</strong>
   </td>
   <td><strong>  Tпреб</strong>
   </td>
   <td><strong>  Tбуф</strong>
   </td>
   <td><strong>  Tобсл</strong>
   </td>
   <td><strong>  Дбуф</strong>
   </td>
   <td><strong>  Добсл</strong>
   </td>
  </tr>
  <tr>
   <td>Здоровые         
   </td>
   <td>13553
   </td>
   <td>   0.13
   </td>
   <td>   8.19
   </td>
   <td>  0.19
   </td>
   <td>   8.00
   </td>
   <td> 17.35
   </td>
   <td>   0.00
   </td>
  </tr>
  <tr>
   <td>Инфец.     
   </td>
   <td>6519
   </td>
   <td>   0.13
   </td>
   <td>   8.19
   </td>
   <td>  0.19
   </td>
   <td>   8.00
   </td>
   <td> 16.91
   </td>
   <td>   0.00
   </td>
  </tr>
  <tr>
   <td>Неинфец         
   </td>
   <td>10168
   </td>
   <td>   0.12
   </td>
   <td>   8.19
   </td>
   <td>  0.19
   </td>
   <td>   8.00
   </td>
   <td> 17.33
   </td>
   <td>   0.00
   </td>
  </tr>
</table>




2. Процент отказов слишком велик, но его легко снизить, если мы расширим буфер.

При 3 стульях отказы составляют 6%, что нарушает ограничения, а при 4 стульях максимальное ожидание в очереди слишком велико (21 минута)



3. Поменяем первого студента на врача средней квалификации, такая конфигурация нам тоже не подходит - ограничение на занятость врача нарушается(занятость последнего врача &lt;70%)
4. Чтобы врачи были заняты больше, необходимо либо расширить буфер (что ведет к увеличению максимального времени ожидания), либо убирать врача.
5. Была найдена конфигурация: 3 врача высшего класса +  1 среднего + студент     + + 4 стула, которая удовлетворяет всем ограничениям. Также было проверено, что она является оптимальной, т.к попытки “удешевить” систему приводят либо к нарушению процента отказа, либо к нарушению времени максимального ожидания в буфере.

Максимальное время в буфере 15.56 минут


<table>
  <tr>
   <td><strong>Тип источника  </strong>
   </td>
   <td><strong>  кол-во заявок</strong>
   </td>
   <td><strong>  p отк</strong>
   </td>
   <td><strong>  Tпреб</strong>
   </td>
   <td><strong>  Tбуф</strong>
   </td>
   <td><strong>  Tобсл</strong>
   </td>
   <td><strong>  Дбуф</strong>
   </td>
   <td><strong>  Добсл</strong>
   </td>
  </tr>
  <tr>
   <td>Здоровые       
   </td>
   <td>13553
   </td>
   <td>   0.04
   </td>
   <td>   6.35
   </td>
   <td>  0.81
   </td>
   <td>   5.55
   </td>
   <td> 83.33
   </td>
   <td>  59.09
   </td>
  </tr>
  <tr>
   <td>Инф.     
   </td>
   <td>6519
   </td>
   <td>   0.04
   </td>
   <td>   6.64
   </td>
   <td>  1.08
   </td>
   <td>   5.56
   </td>
   <td>175.04
   </td>
   <td>  60.59
   </td>
  </tr>
  <tr>
   <td>Не Инф.     
   </td>
   <td>10168
   </td>
   <td>   0.04
   </td>
   <td>   6.76
   </td>
   <td>  1.20
   </td>
   <td>   5.56
   </td>
   <td>221.80
   </td>
   <td>  61.17
   </td>
  </tr>
</table>



<table>
  <tr>
   <td>Тип прибора  
   </td>
   <td>  коэф использования
   </td>
  </tr>
  <tr>
   <td>высший      
   </td>
   <td>            	0.88
   </td>
  </tr>
  <tr>
   <td>высший     
   </td>
   <td>                0.84
   </td>
  </tr>
  <tr>
   <td>высший   
   </td>
   <td>            	0.78
   </td>
  </tr>
  <tr>
   <td>средний    
   </td>
   <td>                0.76
   </td>
  </tr>
  <tr>
   <td>студент   
   </td>
   <td>            	0.72
   </td>
  </tr>
</table>


Стоимость конфигурации 4000р за стул и 2900р в час на оплату врачам. 
