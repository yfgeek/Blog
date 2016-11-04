# 浅谈利用xmlhttp读取百度空间文章(ASP) 

> 2009-08-11

<div class="pcs-article-content_ptkaiapt4bxy_baiduscarticle" id="detailArticleContent_ptkaiapt4bxy_baiduscarticle">
 <p>
  其实我对xmlhttp并不熟悉，只是网上看来的一些代码而已。在这里，我只是
  <strong>
   班门弄斧
  </strong>
  了。而且我只会弄asp网页，对于静态网页，也一定可以实现（详见monyer的部分代码）。
 </p>
 <p>
  这种类似的文章我在BAIDU.EC发过，可惜现在该论坛里的ECSS版块变成了私密板块（我是版主，也进不去，晕），
  <strong>
   为了方便大家，如果有人有自己的独立域名+空间的话，又想加入自己的百度空间更新文章的话，可以借鉴一下该方法。
  </strong>
 </p>
 <p>
  事实上，我已经做好了一个“模块”（没有华丽的模板，只是文字，一个结构而已）。
 </p>
 <p>
  <strong>
   由于网址有误，请大家自行测试！
  </strong>
 </p>
 <p>
  在这里我仅仅介绍一下该网页的核心代码：
 </p>
 <p>
  <code>
   &lt;%
   <br/>
   Set http=Server.CreateObject("Microsoft.XMLHTTP")
   <br/>
   http.Open "GET","
   <br/>
   http.send
   <br/>
   Set xml=Server.CreateObject("Microsoft.XMLDOM")
   <br/>
   xml.Async=False
   <br/>
   xml.ValidateOnParse=False
   <br/>
   xml.Load(http.ResponseXML)
   <br/>
   Set item=xml.getElementsByTagName("item")
   <br/>
   For i=0 To (item.Length-1)
   <br/>
   Set title=item.Item(i).getElementsByTagName("title")
   <br/>
   Set link=item.Item(i).getElementsByTagName("link")
   <br/>
   Set weblog=item.Item(i).getElementsByTagName("description")
   <br/>
   Response.Write("&lt;a href=" &amp; link.Item(0).Text &amp; "&gt;" &amp; title.Item(0).Text &amp;"&lt;/a&gt;&lt;br /&gt;")
   <br/>
   Response.Write("&lt;p&gt;"&amp; weblog.Item(0).Text &amp;"&lt;/p&gt;")
   <br/>
   <br/>
   Next
   <br/>
   %&gt;
  </code>
 </p>
 <p>
  这就是index.asp的核心部分，当然了，这就是典型的asp代码了。
 </p>
 <p>
  &lt;%...%&gt;表示动态代码开始执行
 </p>
 <p>
  很显然，xmlhttp读取的是hi.baidu.com/yfboke/rss，大家的当然是hi.baidu.com/空间ID/rss咯
 </p>
 <p>
  大家可以打开hi.baidu.com/yfboke/rss看看里面到底有什么。
 </p>
 <p>
  打开后大家看到：一个item类。
 </p>
 <p>
  打开它
 </p>
 <p>
  很显然里面有title link description pubdate category author 等几项。
 </p>
 <p>
  意思分别为 标题 连接 内容简写 日期 分类 作者 。。
 </p>
 <p>
  再回到asp代码上。
 </p>
 <p>
  看到       Set title=item.Item(i).getElementsByTagName("title")
 </p>
 <p>
  这一句定义了 title一个变量为rss中的title中的内容。
 </p>
 <p>
  以下代码以此类推。
 </p>
 <p>
  所以。。我们就可以得到：      Response.Write("&lt;a href=" &amp; link.Item(0).Text &amp; "&gt;" &amp; title.Item(0).Text &amp;"&lt;/a&gt;&lt;br /&gt;")
 </p>
 <p>
  这句话的意思就是写了添加一个标题并附上超级链接。（需要一定的asp和html基础才能理解。）
 </p>
 <p>
  所以就是这样。。以此类推。
 </p>
 <p>
  （我只是班门弄斧，不要BS我，我ASP很差的。）
 </p>
 <p>
 </p>
 <p>
  <strong>
   PS:WF(EleoFun)提供了一个思路，我觉得很好，顺便复制和修改了一下，这是“采集”功能，能原汁原味的采集。
  </strong>
 </p>
 <p>
  <code>
   &lt;%
   <br/>
   Function GetContent(str,start,last,n)
   <br/>
   If Instr(lcase(str),lcase(start))&gt;0 then
   <br/>
   select case n
   <br/>
   case 0
   <br/>
   GetContent=Right(str,Len(str)-Instr(lcase(str),lcase(start))-Len(start)+1)
   <br/>
   GetContent=Left(GetContent,Instr(lcase(GetContent),lcase(last))-1)
   <br/>
   case 1
   <br/>
   GetContent=Right(str,Len(str)-Instr(lcase(str),lcase(start))+1)
   <br/>
   GetContent=Left(GetContent,Instr(lcase(GetContent),lcase(last))+Len(last)-1)
   <br/>
   case 2
   <br/>
   GetContent=Right(str,Len(str)-Instr(lcase(str),lcase(start))-Len(start)+1)
   <br/>
   end select
   <br/>
   Else
   <br/>
   GetContent=""
   <br/>
   End if
   <br/>
   End function
   <br/>
   Function GetPage(url)
   <br/>
   dim Http
   <br/>
   set Http=server.createobject("MSXML2.XMLHTTP")
   <br/>
   Http.open "GET",url,false
   <br/>
   Http.send()
   <br/>
   GetPage = Http.responseText
   <br/>
   End Function
   <br/>
   Pageurl = "
   <a href="http://hi.baidu.com/yfboke">
    <strong>
     http://hi.baidu.com/yfboke
    </strong>
   </a>
   "
   <br/>
   Pagebody = GetPage(Pageurl)
   <br/>
   HomeBody = GetContent(Pagebody,"&lt;div id=""header""&gt;","&lt;div id=""ft""&gt;",0)
   <br/>
   Response.Write(HomeBody)
   <br/>
   %&gt;
  </code>
 </p>
</div>


