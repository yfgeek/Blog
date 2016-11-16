---
author: ivan
comments: true
date: 2013-05-06 11:08:14+00:00
layout: post
link: http://www.yfgeek.com/old/2013/05/06/wordpress%e6%a8%a1%e6%9d%bf%e9%81%87%e5%88%b0%e7%9a%84%e9%97%ae%e9%a2%98%e5%8f%8a%e8%a7%a3%e5%86%b3%e5%8a%9e%e6%b3%95/
slug: wordpress%e6%a8%a1%e6%9d%bf%e9%81%87%e5%88%b0%e7%9a%84%e9%97%ae%e9%a2%98%e5%8f%8a%e8%a7%a3%e5%86%b3%e5%8a%9e%e6%b3%95
title: Wordpress模板遇到的问题及解决办法
wordpress_id: 130
categories:
- Web
---

![9](http://www.yfgeek.com/wp-content/uploads/2013/05/9.jpg)
<!-- more -->
在制作WP模板的时候，遇到了好多问题，不过现在都解决了。

一边学习，一遍实践。

问题多多，正在陆续补充当中……

稍有不当，欢迎批评指教！


# 编码问题——UTF-8有无BOM的区别


开始我以为 UTF-8编码没有问题，但在生成的网页中却出现了 head的内容跑到了body里面去的问题。

![未命名](http://www.yfgeek.com/wp-content/uploads/2013/05/未命名.jpg)

并且出现了 一堆“”这种符号。

这是由于UTF-8与UTF-8 无BOM 编码的区别。


<blockquote>The byte-order mark (BOM) in HTML

(via [http://www.w3.org/International/questions/qa-utf8-bom](http://www.w3.org/International/questions/qa-utf8-bom))</blockquote>


解决方法：

将所有的文件改为：

![未命名1](http://www.yfgeek.com/wp-content/uploads/2013/05/未命名1.jpg)

即可。


# 简单的阅读量，主页 统计


由于自己还不会php，只能看懂一些，就百度到了一个比较实用的代码，并且根据代码修改了一个专门统计主页的代码

functions.php

[php][/php]

/*统计 阅读量*/

function getPostViews($postID){
$count_key = 'post_views_count';
$count = get_post_meta($postID, $count_key, true);
if($count==''){
delete_post_meta($postID, $count_key);
add_post_meta($postID, $count_key, '0');
return "0";
}
return $count ;
}
function setPostViews($postID) {
$count_key = 'post_views_count';
$count = get_post_meta($postID, $count_key, true);
if($count==''){
$count = 0;
delete_post_meta($postID, $count_key);
add_post_meta($postID, $count_key, '0');
}else{
$count++;
update_post_meta($postID, $count_key, $count);
}
}
/*首页访问次数统计*/
function getindexview(){
$count_key = 'index_view';
$count = get_post_meta(1, $count_key, true);
if($count==''){
delete_post_meta(1, $count_key);
add_post_meta(1, $count_key, '0');
return "0";
}
return $count ;
}
function setindexview() {
$count_key = 'index_view';
$count = get_post_meta(1, $count_key, true);
if($count==''){
$count = 0;
delete_post_meta(1, $count_key);
add_post_meta(1, $count_key, '0');
}else{
$count++;
update_post_meta(1, $count_key, $count);
}
}

[php][/php]

调用方法：
阅读量的在 页面下：
/<?php setPostViews(get_the_ID()); ?>

阅读量：<?php echo getPostViews(get_the_ID()); ?>
主页统计的在index.php下 ：
/<?php setindexview(); ?>

已经被访问<?php echo getindexview(); ?>次
方法较为粗略 高手见笑。

未完待续
