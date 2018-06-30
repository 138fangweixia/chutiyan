# coding:utf-8
import unittest
import requests
import json
import time
import datetime

#headerss =[{"apsid":"e2ed375b8b2829ea3fe4b3a23a33b8da"}]

headerss =[
           {"apsid":"aab9b86926f0d9fffb6167619f10c638"},#1
           #{"apsid":"e2ed375b8b2829ea3fe4b3a23a33b8da"},zhiyuan
           {"apsid":"b5057e0021b79355ba0b709cef3ff8a1"},#2
           {"apsid":"f721e0382aa8dc30b631494772b85698"},
           {"apsid":"63bb134c15cebb34e4009bcd7291b170"},
           {"apsid":"c63537eac2fc242f0d05a7ab97d5bbac"},
           {"apsid":"f00a30137e9c840a48e1d8e6494ace20"},
           {"apsid":"7b108cbb76896a55b875a0f4ea3ac454"},
           {"apsid":"e2ed375b8b2829ea3fe4b3a23a33b8da"},  
           {"apsid":"6b3fd9cc172c351bd0d835914588bf3b"},  
           {"apsid":"36d5ddc71abd3661e5c87057fb9d7cf2"},
           {"apsid":"8446a3058036496adb2e8ca5286b6c1d"},
           {"apsid":"a421ef69544882018a70a508a349e094"},
           {"apsid":"88bd8e9d29451c728a9f44b2ebd13feb"},
           #{"apsid":"0b3d0cb4a52d5e7041f97a977f3556a6"},me
           {"apsid":"7607b4338212da120ece31d5c6de602c"},
           {"apsid":"1e12b4d55e13a816e87a68484dc98c73"},
           {"apsid":"e442e74400d0d1e4483e61b813fca66d"},
           {"apsid":"847a8bcef1ccb72806c21f6c34e9b5e9"},
           
           {"apsid":"59f4c0c5953bc47fbe402eca467eb3c7"},
           {"apsid":"5a3f7a192deec52c49227b46e99b1222"},
           {"apsid":"1ab286d8f7eff7329e63824244a3c116"},
           {"apsid":"0cfb711ac91cbf69bc4c6fc6bd79e127"},
           {"apsid":"ffd6bc2d5db276bcf3d824037188442e"},
           {"apsid":"1d9ff2992c5613a1883fcf8085636045"},
           {"apsid":"14266263025e07bf159907ccfbae5da1"},

           {"apsid":"a51de4fb631d2352d503a94453fe5c87"},
           {"apsid":"100d6b00d14dd63a51bd09d79a9d9df4"},
           {"apsid":"d868680f00d872ddfbe4d7dabc928081"},
           {"apsid":"e29e6011ced47eef6e0e4617cef4ed42"},
           {"apsid":"ad0d50b59b93b14bbf231703fe05d6da"},
           {"apsid":"e1587b077c943874ded44d073b4ca698"},

           {"apsid":"100d6b00d14dd63a51bd09d79a9d9df4"},
           {"apsid":"d868680f00d872ddfbe4d7dabc928081"},
           {"apsid":"e29e6011ced47eef6e0e4617cef4ed42"},
           {"apsid":"ad0d50b59b93b14bbf231703fe05d6da"},
           {"apsid":"e1587b077c943874ded44d073b4ca698"},           
           
           {"apsid":"b305769c55f0ed71eabb879f40da6a6a"},
           {"apsid":"10bf79a49be836ee11a7ad4e1295d8ab"},
           {"apsid":"8a04fb82ae4d756e6cc7192bb2628669"},
           {"apsid":"264ed28d154c580d3f2b82a9f25dfd1b"},
           {"apsid":"c701910701e0cd9165ccf0301622a3e2"},

           {"apsid":"0cbbd22c3c4fcdc0ccf689c010cf7954"},
           {"apsid":"f066ebf9266cc9fcc3b851d4286846f9"},
           {"apsid":"eb3aa6afaf3ce3a87b700387893b0c3e"},
           {"apsid":"9c1aa78263689df9607ea83e7ede5a43"},
           {"apsid":"aeb7c5174715582f9dde17d9116d78a3"},
           {"apsid":"04ea4ccee49e09ffa44161375638da2a"},
           {"apsid":"512ea1cf04524b5dd9c09dac1b11a19f"},
           {"apsid":"8929f8157f59919d6b4cb192f471b768"},
           {"apsid":"78d12128e880562ab7b8181fdc14bb6c"},
           {"apsid":"34cb94d5b65394d63f625b6471847f4b"},
           {"apsid":"010684b0aa92443dbd347418d00b6516"},           
           {"apsid":"9794e23e16863c72fde8e2d527e2644b"},
           {"apsid":"3a0ef27766ad411f7e20eb912a0efccf"},
           {"apsid":"43c7bc7c5e5b3945e1070ad77fd15bb7"},
           {"apsid":"8521b48bdb4363148ddc294485ca223c"},
           {"apsid":"95a24c2ae56f86e5efafd8c391acc81d"},
           
           
           {"apsid":"6993bccb7b0efe92db9acfb9ddf1ee65"},
           {"apsid":"c5c293e70cad751abe6513c7c381c984"},
           {"apsid":"67b936f56f21dd4121afd268e43edd84"},
           {"apsid":"cad604ddc2d1b26c14fe969edb86ffc8"},
           {"apsid":"af600a7b55e45192412f2282c4ca41b3"},           
           {"apsid":"dedcdc97bb669cf55264d6ee444ba1aa"},
           {"apsid":"5f7ded03b62c5045fceca34dfbd0efb9"},
           {"apsid":"1b6a811930d81950066380e565e550a2"},
           {"apsid":"42453032c16c466fabf497b8367a20f6"},
           {"apsid":"5d8c2ee3acdd3af32f7322127c81e670"},
           {"apsid":"5af3563d5309bd557cfe46743a76ec03"},
           {"apsid":"300122c670e1c3ebc6c18e62640e883e"},
           
           {"apsid":"fc361c58fcaaf4f92c0f17844164fd0a"},
           {"apsid":"f745300ef7521a054e648a248d4e53ec"},
           {"apsid":"67a855da7e1790b89548930efdb0a242"},
           {"apsid":"41fefbcbfd12057387826f09b8f78cc8"},
           {"apsid":"8508e9599fd566356f1c57148c2e1250"},
           {"apsid":"7fb7d9ed2209a988c6e17911b35ebfa7"},
           {"apsid":"adf56f2e348906557aa7b223bb906af1"},
           {"apsid":"55daac547d7d07c1cb15dbdf4c685e55"},
           {"apsid":"e18b76f461776eb17187d4eb52b2b57d"},
           {"apsid":"542935661fe8a595245fea2cae45d9cb"},
           {"apsid":"2e4a52cf2d3c6211b990f37678c3553e"},
           {"apsid":"1861e9848b7f7a11326ee9a39decc381"},
           {"apsid":"8d94f4b6e72bf22ed5ba1475fe203994"},
           {"apsid":"8c782a8053e688320c6fbd52b771883d"},
           {"apsid":"b87ca45bd026b4db6cc811436be29f62"},
           {"apsid":"a15e172217842e68a82e022eb045cd15"},

           {"apsid":"299896b736bd8eb7314678526ab04bdc"},
           {"apsid":"e08fdbe8ef5b3ac0938cd1e46e6a24d2"},
           {"apsid":"69eb4fe2822901b9a283ed5714184542"},
           {"apsid":"e835289f3c91a4ed8ff2be993e13b71c"},
           {"apsid":"fa21de69ef12e0075a7ca7caae0a3145"},
           {"apsid":"88131fb7c78d73d2d9ef38c49bba97fa"},
           {"apsid":"7c96dc1f43a9feb8efc7657ed08fde74"},
           {"apsid":"f2b93f4d7c33315bad42aa1e2b794a3c"},
           {"apsid":"272d30fcf5690bcdfdeb19ad42a13311"},
           {"apsid":"2045b9c20498aa8a23bbb662837ab32b2"},

           {"apsid":"3dca18afcc20c6b03701a275ea0b61f2"},
           {"apsid":"df357a5e479acd73bf681f1b2e93085d"},


           
           {"apsid":"7949aa3e7ca25bd72d01fdecc5aef34d"},
           {"apsid":"0a33e2793c2eaaf3a480aaa6c79c90c5"},
           {"apsid":"41d1b9d6386601223818a12866aa6296"},
           {"apsid":"09ff9edbc07d0b886a8645269b502e5e"},
           {"apsid":"2e208023501645374df9b0f1eb3d7a51"},

           ]

#正常创建的课程 3.2第一次批量 3.3能不能也批量？        
number = 0
for headers in headerss:
    

   
    nowtime=datetime.datetime.now()#获取当前时间
    record_at=nowtime.strftime('%Y-%m-%dT%H:%M:%SZ') #打卡日期、学员打卡时间
    
    url4 = "https://apiopen3t.jingdaka.com/user/submit"#学员提交打卡课程
    
    content="2018.6.20 鲸打卡——让老师更省心地改作业，让学员更开心地晒作业。"+str(number)

    payload = {"course_id":3415,
            
            "password":"",
             "record_at":record_at,
             "content":content,"picture_list":["2018/03/12/tmp/wx729ab39fca33e5d6.o6zAJsyj2jQ5GnjhE0xl-VAKOhOs.7af12255d9c805c0e430b405f94af653.png"],"video_list":[],"voice_list":[{"voice":"2018/02/02/5a2ea5b9-eba6-4429-bc5a-244eca4a8071.silk","voice_duration":3}],
              "form_id":"the formId is a mock one","web_title":"推荐鲸打卡——在线教育工作者的神器","website":"https://mp.weixin.qq.com/s/1UIfRkzLgh7zuRIDnFC-QQ"
           }
    
    data_json = json.dumps(payload)
    r = requests.post(url4,headers=headers,data=data_json)
    print (r.text)
    
    j = json.loads(r.text)
    err_msg = j["err_msg"]
    
    if err_msg ==  "SUCCESS":
        number=number+1
    
    print(content)
    time.sleep(3)
    
    


   
