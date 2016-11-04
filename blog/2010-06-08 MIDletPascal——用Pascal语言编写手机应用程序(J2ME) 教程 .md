# MIDletPascal——用Pascal语言编写手机应用程序(J2ME) 教程 

> 2010-06-08

<div class="pcs-article-content_ptkaiapt4bxy_baiduscarticle" id="detailArticleContent_ptkaiapt4bxy_baiduscarticle">
 <p>
  <img class="blogimg" small="0" src="images/c6392fa75767515533fcd7e465672f15.jpg"/>
  <br/>
  <br/>
  MIDletPascal，好软件，个人感觉很不错很不错。
 </p>
 <p>
  因为在编程领域，我非常熟悉object pascal语言，MIDletPascal是以object pascal为标准的编译器，可以用pascal语言编写手机软件游戏（J2ME）。
 </p>
 <p>
  下载试了试，很容易操作
 </p>
 <p>
  使用object pascal语言的IDE还有delphi,turbo pascal,free pascal,lazarus等等，但他们都是直接编译／解释成可执行文件EXE
 </p>
 <p>
  今天无意间找到了如此神通广大的软件，先膜拜两下
 </p>
 <p>
  <strong>
   第一步：下载及安装
  </strong>
 </p>
 <p>
  首先但我的网盘上下载
 </p>
 <p>
  下载地址：
  <a href="http://www.uushare.com/user/yfblog/file/3114603">
   http://www.uushare.com/user/yfblog/file/3114603
  </a>
 </p>
 <p>
  解压缩后，得到如下：
 </p>
 <p>
  小型java模拟器.exe
  <br/>
  MPInstall2.exe
  <br/>
  中文版使用说明.txt
  <br/>
  MpIDE.exe
  <br/>
  MPHelp_ru.chm
 </p>
 <p>
  首先运行MPInstall2.exe，安装它待安装完毕后。
 </p>
 <p>
  把MpIDE.exe复制到安装目录，替换原程序（汉化过程）
 </p>
 <p>
  然后打开MpIDE.exe，菜单栏-配置-注册信息。
 </p>
 <p>
  user: Albert Einstein
  <br/>
  code: D6Qw8p1CHW7xY7D
 </p>
 <p>
  关闭它。
 </p>
 <p>
  然后再安装，小型java模拟器.exe即可。
 </p>
 <p>
  下载再启动MIDLETPASCAL的时候，就完美了。
 </p>
 <p>
  <strong>
   第二步：熟悉开发环境
  </strong>
 </p>
 <p>
  打开开始菜单-所有程序中的MIDletPascal 2软件。
 </p>
 <p>
  进入如图的软件界面：
 </p>
 <p>
  <img class="blogimg" small="0" src="images/1090790edafb65e38f060aa834c392d2.jpg"/>
 </p>
 <p>
  对于这种开发环境，经常使用delphi或lazurus的用户是很熟悉的。
 </p>
 <p>
  下面我们来写我们第一个J2ME程序——hello world
 </p>
 <p>
  文件-新建工程
 </p>
 <p>
  <img class="blogimg" small="0" src="images/547e999d198de8f4d975b78a626a1cca.jpg"/>
  <br/>
  <br/>
  很明显，右边是编辑框，左边工程的设置下面是编译信息。
 </p>
 <p>
  <img class="blogimg" small="0" src="images/2af48f1ff44bd6cc3968830aa6c20611.jpg"/>
 </p>
 <p>
  下面我来解释下代码：
 </p>
 <code>
  <p>
   program HelloWorld;      {这个是设置J2ME程序名称}
   <br/>
   begin                               {程序开始}
   <br/>
   drawText('Hello world!', 0, 0); {使用drawtext过程 让手机屏幕上显示 HELLO WORLD字样，坐标为0,0}
   <br/>
   repaint;                                        {绘图}
   <br/>
   delay(2000);                                {2000毫秒后结束该程序}
   <br/>
   end.
   <br/>
  </p>
 </code>
 <p>
  比起J2ME语言来说，虽然不如JAVA语言简单开放，但是比java语言严谨，易懂。
 </p>
 <p>
  好了，开始编译，按下F7开始编译。
 </p>
 <p>
  一会就看到了编译成功的字样。
 </p>
 <p>
  找到工程目录\bin\下
 </p>
 <p>
  会发现两个文件，一个是jar文件，一个是jad文件。
 </p>
 <p>
  双击那个jar文件，会用手机顽童打开。
 </p>
 <p>
  <img class="blogimg" small="0" src="images/c04de322a40037754f2d525150e5b52e.jpg"/>
 </p>
 <p>
  经过20秒后，程序自动结束。我们的第一个helloworld程序，就这样开发完毕了。
 </p>
 <p>
  <strong>
   第三步：MIDlet Pascal的函数和过程
  </strong>
 </p>
 <p>
  在语法，变量上，是和freepascal完全一样的，不过midlet有很多函数和过程。
 </p>
 <p>
  下面介绍一下。
 </p>
 <p>
  所有函数，过程如下：
 </p>
 <code>
  <p>
   drawArc                                drawEllipse                                  drawImage
   <br/>
   drawLine                                   drawRect                              drawRoundRect
   <br/>
   drawText                                fillEllipse                                   fillRect
   <br/>
   fillRoundRect                               getColorBlue                              getColorGreen
   <br/>
   getColorRed                               getColorsNum                                  getHeight
   <br/>
   getImageHeight                              getImageWidth                            getStringHeight
   <br/>
   getStringWidth                                   getWidth                             isColorDisplay
   <br/>
   loadImage                                       plot                                    repaint
   <br/>
   setClip                                   setColor                             setDefaultFont
   <br/>
   setFont                              getKeyClicked                              getKeyPressed
   <br/>
   keyToAction                                      delay                             getCurrentTime
   <br/>
   getDay                                    getHour                                  getMinute
   <br/>
   getMonth                          getRelativeTimeMs                                  getSecond
   <br/>
   getWeekDay                                    getYear                                 getYearDay
   <br/>
   abs                                       acos                                       asin
   <br/>
   atan                                      atan2                                        cos
   <br/>
   exp                                       frac                                        log
   <br/>
   log10                                        pow                                       rabs
   <br/>
   sin                                        sqr                                       sqrt
   <br/>
   tan                                  toDegrees                                  toRadians
   <br/>
   trunc                                       copy                                    getChar
   <br/>
   integerToString                                     length                                     locase
   <br/>
   pos                                    setChar                            stringToInteger
   <br/>
   stringToReal                                     upcase                                 addCommand
   <br/>
   choiceAppendString                    choiceAppendStringImage                     choiceGetSelectedIndex
   <br/>
   choiceIsSelected                                  clearForm                              createCommand
   <br/>
   emptyCommand                              formAddChoice                               formAddGauge
   <br/>
   formAddImage                               formAddSpace                              formAddString
   <br/>
   formAddTextField                                formGetText                               formGetValue
   <br/>
   formRemove                                formSetText                               formSetValue
   <br/>
   getClickedCommand                           getTextBoxString                           menuAppendString
   <br/>
   menuAppendStringImage                       menuGetSelectedIndex                             menuIsSelected
   <br/>
   playAlertSound                              removeCommand                                  setTicker
   <br/>
   showAlert                                 showCanvas                                   showForm
   <br/>
   showMenu                                showTextBox                        addRecordStoreEntry
   <br/>
   closeRecordStore                          deleteRecordStore                     deleteRecordStoreEntry
   <br/>
   getRecordStoreSize                            openRecordStore                       readRecordStoreEntry
   <br/>
   addHttpBody                              addHttpHeader                                  closeHttp
   <br/>
   getHttpHeader                            getHttpResponse                                 isHttpOpen
   <br/>
   openHttp                            sendHttpMessage                              setHttpMethod
   <br/>
   smsIsSending                               smsStartSend                          smsWasSuccessfull
   <br/>
   getPlayerDuration                                 openPlayer                             setPlayerCount
   <br/>
   startPlayer                                 stopPlayer                              closeResource
   <br/>
   openResource                                   readByte                                   readLine
   <br/>
   resourceAvailable                                     assert                                        chr
   <br/>
   debug                                getProperty                                       halt
   <br/>
   isMidletPaused                                        odd                                        ord
   <br/>
   random                                  randomize
  </p>
 </code>
 <p>
  未完待续。。。
  <br/>
 </p>
</div>


