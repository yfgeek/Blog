# Fibonacci(斐波那契)数列 pascal程序代码 

> 2009-10-30

<div class="pcs-article-content_ptkaiapt4bxy_baiduscarticle" id="detailArticleContent_ptkaiapt4bxy_baiduscarticle">
 <p>
  自习课利用十分钟自学了书上面的数组 函数 过程
  <br/>
  看到了一个数列，是Fibonacci
  <br/>
  先说一下什么是Fibonacci数列,即斐波那契数列。
  <br/>
  它的特点是前面两个数的和等于后面的一个数。斐波那契数列只有一个。
  <br/>
  例如1，1，2，3，5，8，13，21，34，55，89，144，233，377，610，987，1597，2584，4181，6765……
  <br/>
  至于这个简单的程序怎么编写，我想到了很多方法，比如 递归 数组 等等
  <br/>
  最终还是用数组比较直观，因为它是数学表达式吧
  <br/>
  到最后才发现，我写的程序竟然跟网上类似。晕
  <br/>
  没关系，那我也打上来了
  <br/>
  <code>
   program abqlsl;
   <br/>
   var
   <br/>
   a:array [0..20] of integer;
   <br/>
   i:integer;
   <br/>
   begin
   <br/>
   write('0 1');
   <br/>
   a[0]:=0;
   <br/>
   a[1]:=1;
   <br/>
   for i:=2 to 20 do
   <br/>
   begin
   <br/>
   a[i]:=a[i-1]+a[i-2];
   <br/>
   write(' ',a[i]);
   <br/>
   end;
   <br/>
   readln
   <br/>
   end.
   <br/>
  </code>
  具体解释以后再加吧
  <br/>
  目前，正在想另外一个比较难的题…
  <br/>
  说实在的，编程挺有趣的…
 </p>
</div>


