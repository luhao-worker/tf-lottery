<?php
header("Content-type:text/html;charset=utf-8");  
error_reporting(E_ALL^E_NOTICE^E_WARNING);
ini_set("memory_limit","-1");
set_time_limit(0);
$file = file_get_contents('items.json');
$res = json_decode($file,true);

foreach($res as $a=>$b){//总循环
    foreach ($b['ask_content'] as $i=>$j){       //单个提问内容循环 
        $j =DeleteHtml($j);
        $ask_content .= $j;
    }
    //echo $b['ask_id'][0];
    //echo '<br/>';
    foreach ($b['answer'] as $k=>$q){      //多个回答以及讨论循环
        foreach ($q['answer_content'] as $kk=>$qq){         //多个回答内容循环
        $qq =DeleteHtml($qq);
        $answer_content .= $qq;
    }
    
        
     
    /**********模拟多个问答对话***********/
    
    echo $ask_content; //echo '问';
    echo '<br/>';
    echo $answer_content;  //echo '答';
    echo '<br/>';
    unset($answer_content);
    

    foreach ($q['topic_list'] as $z=>$w){         //多个讨论内容循环
         foreach ($q['topic_list'][$z]['topic_list_content'] as $zz=>$ww){
            $ww =DeleteHtml($ww);
            $topic_list_content .= $ww;          
         }
    
     if(count($q['topic_list'])%2 == 0){ 
       echo $topic_list_content;  //echo '讨';
       echo '<br/>'; }
     unset($topic_list_content);
    }
       
        
 
     /**********模拟多个讨论对话***********/
   
   
    }unset($ask_content);
     
    
}


function DeleteHtml($str) 
{ 
$str = trim($str); //清除字符串两边的空格
$str = preg_replace("/\t/","",$str); //使用正则表达式替换内容，如：空格，换行，并将替换为空。
$str = preg_replace("/\r\n/","",$str); 
$str = preg_replace("/\r/","",$str); 
$str = preg_replace("/\n/","",$str); 
$str = preg_replace("/ /","",$str);
$str = preg_replace("/  /","",$str);  //匹配html中的空格
return trim($str); //返回字符串
}

?>

