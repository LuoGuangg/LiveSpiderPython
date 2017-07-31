def getAdict():

    douYuDotaUrl = "https://www.douyu.com/directory/game/DOTA2"
    douYuLolUrl = "https://www.douyu.com/directory/game/LOL"
    douYuDnfUrl = "https://www.douyu.com/directory/game/DNF"
    douYuCsUrl = "https://www.douyu.com/directory/game/cs"
    douYuHowUrl = "https://www.douyu.com/directory/game/How"
    douYuOWUrl = "https://www.douyu.com/directory/game/Overwatch"
    douYuMeiNvUrl = "https://www.douyu.com/directory/game/yz"
    douYuMeiNvUrl1 = "https://www.douyu.com/directory/game/xx"
    douYuMeiNvUrl2 = "https://www.douyu.com/directory/game/ecy"
    douYuZhuJiUrl = "https://www.douyu.com/directory/game/TVgame"
    douYuTiaoSanUrl = "https://www.douyu.com/directory/game/jdqs"
    douYuTiaoSanUrl1 = "https://www.douyu.com/directory/game/TSQS"

    douYuUrlHead = "https://www.douyu.com"
    douYuXPath = {
        'titles':'//li/a[@class="play-list-link"]/div[@class="mes"]/div[@class="mes-tit"]/h3[@class="ellipsis"]/text()',
        'imgs':'//li/a[@class="play-list-link"]/span[@class="imgbox"]/img/@data-original',
        'nums':'//li/a[@class="play-list-link"]//span[@class="dy-num fr"]/text()',
        'names':'//li/a[@class="play-list-link"]/div[@class="mes"]//span[@class="dy-name ellipsis fl"]/text()',
        'urls':'//li/a[@class="play-list-link"]/@href',
        }

    pandaDotaUrl = "https://www.panda.tv/cate/dota2"
    pandaLolUrl = "https://www.panda.tv/cate/lol"
    pandaDnfUrl = "https://www.panda.tv/cate/dnf"
    pandaCsUrl = "https://www.panda.tv/cate/csgo"
    pandaHowUrl = "http://www.panda.tv/cate/hearthstone"
    pandaOWUrl = "http://www.panda.tv/cate/overwatch"
    pandaMeiNvUrl = "https://www.panda.tv/cate/yzdr"
    pandaZhuJiUrl = "http://www.panda.tv/cate/zhuji"
    pandaTiaoSanUrl = "https://www.panda.tv/cate/pubg"
    pandaTiaoSanUrl1 = "https://www.panda.tv/cate/ttts"

    pandaUrlHead = "https://www.panda.tv"
    pandaXPath = {
        'titles':'//a[@class="video-list-item-wrap"]/div[@class="video-info"]/span[@class="video-title"]/text()',
        'imgs':'//a[@class="video-list-item-wrap"]/div[@class="video-cover"]/img/@data-original',
        'nums':'//a[@class="video-list-item-wrap"]/div[@class="video-info"]/span[@class="video-number"]/text()',
        'names':'//div[@class="user-info"]/div[@class="userinfo-desc"]/span[@class="userinfo-nickname"]/text() | //a[@class="video-list-item-wrap"]/div[@class="video-info"]/span[@class="video-nickname"]/text() ',
        'urls':'//a[@class="video-list-item-wrap"]/@href',
        }


    huyaDotaUrl = "http://www.huya.com/g/7"
    huyaLolUrl = "http://www.huya.com/g/lol"
    huyaDnfUrl = "http://www.huya.com/g/dnf"
    huyaCsUrl = "http://www.huya.com/g/cs"
    huyaHowUrl = "http://www.huya.com/g/393"
    huyaOWUrl = "http://www.huya.com/g/2174"
    huyaMeiNvUrl = "http://www.huya.com/g/xingxiu"
    huyaZhuJiUrl = "http://www.huya.com/g/1964"
    huyaTiaoSanUrl = "http://www.huya.com/g/2793"
    huyaTiaoSanUrl1 = "http://www.huya.com/g/1902"

    huyaUrlHead = ""
    huyaXPath = {
        'titles':'//li[@class="game-live-item"]/a[@class="title new-clickstat"]/@title',
        'imgs':'//li[@class="game-live-item"]/a[@class="video-info new-clickstat"]/img/@data-original',
        'nums':'//li[@class="game-live-item"]/span[@class="txt"]/span[@class="num"]/i[@class="js-num"]/text()',
        'names':'//li[@class="game-live-item"]/span[@class="txt"]/span[@class="avatar fl"]/i/text()',
        'urls':'//li[@class="game-live-item"]/a[@class="video-info new-clickstat"]/@href',
        }


    longzhuDotaUrl = "http://longzhu.com/channels/dota2"
    longzhuLolUrl = "http://longzhu.com/channels/lol"
    longzhuDnfUrl = "http://longzhu.com/channels/dnf?from=figame"
    longzhuCsUrl = "http://longzhu.com/channels/csgo"
    longzhuOWUrl = "http://longzhu.com/channels/ow?from=left"
    longzhuMeiNvUrl = "http://longzhu.com/channels/hwzb?from=figame"
    longzhuZhuJiUrl = "http://longzhu.com/channels/djzjjj?from=left"
    longzhuTiaoSanUrl = "http://longzhu.com/channels/h1z1"
    longzhuTiaoSanUrl1 = "http://longzhu.com/channels/jdqs?from=left"

    longzhuUrlHead = ""
    longzhuXPath = {
        'titles':'//div[@class="list-con"]/a[@class="livecard"]/h3[@class="listcard-caption"]/text()',
        'imgs':'//div[@class="list-con"]/a[@class="livecard"]/img[@class="livecard-thumb "]/@src | //div[@class="list-con"]/a[@class="livecard"]/img[@class="livecard-thumb livecard-thumb-suipai"]/@src',
        'nums':'//div[@class="list-con"]/a[@class="livecard"]/ul[@class="livecard-meta"]/li[@class="livecard-meta-item livecard-meta-views"]/span[@class="livecard-meta-item-text"]/text()',
        'names':'//div[@class="list-con"]/a[@class="livecard"]/span[@class="livecard-modal"]/strong[@class="livecard-modal-username"]/text()',
        'urls':'//div[@class="list-con"]/a[@class="livecard"]/@href',
        }   
    
    quanminDotaUrl = "https://www.quanmin.tv/game/dota2"
    quanminLolUrl = "https://www.quanmin.tv/game/lol"
    quanminDnfUrl = "https://www.quanmin.tv/game/dnf"
    quanminCsUrl = "https://www.quanmin.tv/game/csgo"
    quanminOWUrl = "https://www.quanmin.tv/game/overwatch"
    quanminZhuJiUrl = "https://www.quanmin.tv/game/tvgame"
    quanminTiaoSanUrl = "https://www.quanmin.tv/game/juediqiusheng"
    quanminTiaoSanUrl = "https://www.quanmin.tv/game/sanbingzhiwang"

    quanminUrlHead = ""
    quanminXPath = {
        'titles':'//a[@class="common_w-card_href"]/div[@class="common_w-card_bottom"]//p/text()',
        'imgs':'//a[@class="common_w-card_href"]/div[@class="common_w-card_cover-wrap"]/img/@src',
        'nums':'//a[@class="common_w-card_href"]/div[@class="common_w-card_bottom"]//span[@class="common_w-card_views-num"]/text()',
        'names':'//a[@class="common_w-card_href"]/div[@class="common_w-card_bottom"]//span[@class="common_w-card_host-name"]/text()',
        'urls':'//a[@class="common_w-card_href"]/@href',
        }

    huomaoDotaUrl = "https://www.huomao.com/channels/channel.json?page=1&game_url_rule=dota2"
    huomaoLolUrl = "https://www.huomao.com/channels/channel.json?page=1&game_url_rule=lol"
    huomaoDnfUrl = "https://www.huomao.com/channels/channel.json?page=1&game_url_rule=dnf"
    huomaoCsUrl = "https://www.huomao.com/channels/channel.json?page=1&game_url_rule=CSGO"
    huomaoOWUrl = "https://www.huomao.com/channels/channel.json?page=1&page_size=120&game_url_rule=Overwatch"
    huomaoMeiNvUrl = "https://www.huomao.com/channels/channel.json?page=1&game_url_rule=ylxx"
    huomaoTiaoSanUrl = "https://www.huomao.com/channels/channel.json?page=1&game_url_rule=battlegrounds"

    huomaoUrlHead = "https://www.huomao.com/"
    huomaoJsonDir = {
        'title':'channel',
        'img':'image',
        'num':'views',
        'name':'username',
        'url':'room_number',
        'json1':'data',
        'json2':'channelList',
    }

    zhanqiDotaUrl = "https://www.zhanqi.tv/api/static/v2.1/game/live/10/30/1.json"
    zhanqiLolUrl = "https://www.zhanqi.tv/api/static/v2.1/game/live/6/30/1.json"
    zhanqiDnfUrl = "https://www.zhanqi.tv/api/static/v2.1/game/live/22/30/1.json"
    zhanqiHowUrl = "https://www.zhanqi.tv/api/static/v2.1/game/live/9/30/1.json"
    zhanqiOWUrl = "https://www.zhanqi.tv/api/static/v2.1/game/live/82/30/1.json"
    zhanqiMeiNvUrl = "https://www.zhanqi.tv/api/static/v2.1/game/live/65/30/1.json"
    zhanqiTiaoSanUrl = "https://www.zhanqi.tv/api/static/v2.1/game/live/106/30/1.json"

    zhanqiUrlHead = "https://www.zhanqi.tv"
    zhanqiJsonDir = {
        'title':'title',
        'img':'spic',
        'num':'online',
        'name':'nickname',
        'url':'url',
        'json1':'data',
        'json2':'rooms',
    }

    dotaDirs = {
        'douYuUrl':douYuDotaUrl,
        'douYuXPath':douYuXPath,
        'douYuUrlHead':douYuUrlHead,

        'pandaUrl':pandaDotaUrl,
        'pandaXPath':pandaXPath,
        'pandaUrlHead':pandaUrlHead,

        'huyaUrl':huyaDotaUrl,
        'huyaXPath':huyaXPath,
        'huyaUrlHead':huyaUrlHead,

        'longzhuUrl':'',
        'longzhuXPath':'',
        'longzhuUrlHead':'',

        'quanminUrl':quanminDotaUrl,
        'quanminXPath':quanminXPath,
        'quanminUrlHead':quanminUrlHead,

        'huomaoUrl':huomaoDotaUrl,
        'huomaoUrlHead':huomaoUrlHead,
        'huomaoJsonDir':huomaoJsonDir,

        'zhanqiUrl':zhanqiDotaUrl,
        'zhanqiUrlHead':zhanqiUrlHead,
        'zhanqiJsonDir':zhanqiJsonDir,

        'index':1,
        'game':'DOTA2',
                }

    lolDirs = {
        'douYuUrl':douYuLolUrl,
        'douYuXPath':douYuXPath,
        'douYuUrlHead':douYuUrlHead,

        'pandaUrl':pandaLolUrl,
        'pandaXPath':pandaXPath,
        'pandaUrlHead':pandaUrlHead,

        'huyaUrl':huyaLolUrl,
        'huyaXPath':huyaXPath,
        'huyaUrlHead':huyaUrlHead,

        'longzhuUrl':longzhuLolUrl,
        'longzhuXPath':longzhuXPath,
        'longzhuUrlHead':longzhuUrlHead,

        'quanminUrl':quanminLolUrl,
        'quanminXPath':quanminXPath,
        'quanminUrlHead':quanminUrlHead,

        'huomaoUrl':huomaoLolUrl,
        'huomaoUrlHead':huomaoUrlHead,
        'huomaoJsonDir':huomaoJsonDir,

        'zhanqiUrl':zhanqiLolUrl,
        'zhanqiUrlHead':zhanqiUrlHead,
        'zhanqiJsonDir':zhanqiJsonDir,

        'index':2,
        'game':'LOL',
                }

    dnfDirs = {
        'douYuUrl':douYuDnfUrl,
        'douYuXPath':douYuXPath,
        'douYuUrlHead':douYuUrlHead,

        'pandaUrl':pandaDnfUrl,
        'pandaXPath':pandaXPath,
        'pandaUrlHead':pandaUrlHead,

        'huyaUrl':huyaDnfUrl,
        'huyaXPath':huyaXPath,
        'huyaUrlHead':huyaUrlHead,

        'longzhuUrl':longzhuDnfUrl,
        'longzhuXPath':longzhuXPath,
        'longzhuUrlHead':longzhuUrlHead,

        'quanminUrl':quanminDnfUrl,
        'quanminXPath':quanminXPath,
        'quanminUrlHead':quanminUrlHead,

        'huomaoUrl':huomaoDnfUrl,
        'huomaoUrlHead':huomaoUrlHead,
        'huomaoJsonDir':huomaoJsonDir,

        'zhanqiUrl':zhanqiDnfUrl,
        'zhanqiUrlHead':zhanqiUrlHead,
        'zhanqiJsonDir':zhanqiJsonDir,

        'index':3,
        'game':'DNF',
                }

    csDirs = {
        'douYuUrl':douYuCsUrl,
        'douYuXPath':douYuXPath,
        'douYuUrlHead':douYuUrlHead,

        'pandaUrl':pandaCsUrl,
        'pandaXPath':pandaXPath,
        'pandaUrlHead':pandaUrlHead,

        'huyaUrl':huyaCsUrl,
        'huyaXPath':huyaXPath,
        'huyaUrlHead':huyaUrlHead,

        'longzhuUrl':longzhuCsUrl,
        'longzhuXPath':longzhuXPath,
        'longzhuUrlHead':longzhuUrlHead,

        'quanminUrl':quanminCsUrl,
        'quanminXPath':quanminXPath,
        'quanminUrlHead':quanminUrlHead,

        'huomaoUrl':huomaoCsUrl,
        'huomaoUrlHead':huomaoUrlHead,
        'huomaoJsonDir':huomaoJsonDir,

        'zhanqiUrl':'',
        'zhanqiUrlHead':'',
        'zhanqiJsonDir':'',

        'index':4,
        'game':'CSGO',
                }

    howDirs = {
        'douYuUrl':douYuHowUrl,
        'douYuXPath':douYuXPath,
        'douYuUrlHead':douYuUrlHead,

        'pandaUrl':pandaHowUrl,
        'pandaXPath':pandaXPath,
        'pandaUrlHead':pandaUrlHead,

        'huyaUrl':huyaHowUrl,
        'huyaXPath':huyaXPath,
        'huyaUrlHead':huyaUrlHead,

        'longzhuUrl':'',
        'longzhuXPath':'',
        'longzhuUrlHead':'',

        'quanminUrl':'',
        'quanminXPath':'',
        'quanminUrlHead':'',

        'huomaoUrl':'',
        'huomaoUrlHead':'',
        'huomaoJsonDir':'',

        'zhanqiUrl':zhanqiHowUrl,
        'zhanqiUrlHead':zhanqiUrlHead,
        'zhanqiJsonDir':zhanqiJsonDir,

        'index':5,
        'game':'How',
                }

    oWDirs = {
        'douYuUrl':douYuOWUrl,
        'douYuXPath':douYuXPath,
        'douYuUrlHead':douYuUrlHead,

        'pandaUrl':pandaOWUrl,
        'pandaXPath':pandaXPath,
        'pandaUrlHead':pandaUrlHead,

        'huyaUrl':huyaOWUrl,
        'huyaXPath':huyaXPath,
        'huyaUrlHead':huyaUrlHead,

        'longzhuUrl':longzhuOWUrl,
        'longzhuXPath':longzhuXPath,
        'longzhuUrlHead':longzhuUrlHead,

        'quanminUrl':quanminOWUrl,
        'quanminXPath':quanminXPath,
        'quanminUrlHead':quanminUrlHead,

        'huomaoUrl':huomaoOWUrl,
        'huomaoUrlHead':huomaoUrlHead,
        'huomaoJsonDir':huomaoJsonDir,

        'zhanqiUrl':zhanqiOWUrl,
        'zhanqiUrlHead':zhanqiUrlHead,
        'zhanqiJsonDir':zhanqiJsonDir,

        'index':6,
        'game':'OW',
                }

    meiNvDirs = {
        'douYuUrl':douYuMeiNvUrl,
        'douYuUrl1':douYuMeiNvUrl1,
        'douYuUrl2':douYuMeiNvUrl2,
        'douYuXPath':douYuXPath,
        'douYuUrlHead':douYuUrlHead,

        'pandaUrl':pandaMeiNvUrl,
        'pandaXPath':pandaXPath,
        'pandaUrlHead':pandaUrlHead,

        'huyaUrl':huyaMeiNvUrl,
        'huyaXPath':huyaXPath,
        'huyaUrlHead':huyaUrlHead,

        'longzhuUrl':longzhuMeiNvUrl,
        'longzhuXPath':longzhuXPath,
        'longzhuUrlHead':longzhuUrlHead,

        'quanminUrl':'',
        'quanminXPath':'',
        'quanminUrlHead':'',

        'huomaoUrl':huomaoMeiNvUrl,
        'huomaoUrlHead':huomaoUrlHead,
        'huomaoJsonDir':huomaoJsonDir,

        'zhanqiUrl':zhanqiMeiNvUrl,
        'zhanqiUrlHead':zhanqiUrlHead,
        'zhanqiJsonDir':zhanqiJsonDir,

        'index':7,
        'game':'MeiNv',
                }

    zhuJiDirs = {
        'douYuUrl':douYuZhuJiUrl,
        'douYuXPath':douYuXPath,
        'douYuUrlHead':douYuUrlHead,

        'pandaUrl':pandaZhuJiUrl,
        'pandaXPath':pandaXPath,
        'pandaUrlHead':pandaUrlHead,

        'huyaUrl':huyaZhuJiUrl,
        'huyaXPath':huyaXPath,
        'huyaUrlHead':huyaUrlHead,

        'longzhuUrl':longzhuZhuJiUrl,
        'longzhuXPath':longzhuXPath,
        'longzhuUrlHead':longzhuUrlHead,

        'quanminUrl':quanminZhuJiUrl,
        'quanminXPath':quanminXPath,
        'quanminUrlHead':quanminUrlHead,

        'huomaoUrl':'',
        'huomaoUrlHead':'',
        'huomaoJsonDir':'',

        'zhanqiUrl':'',
        'zhanqiUrlHead':'',
        'zhanqiJsonDir':'',

        'index':8,
        'game':'ZhuJi',
                }

    tiaoSanDirs = {
        'douYuUrl':douYuTiaoSanUrl,
        'douYuUrl1':douYuTiaoSanUrl1,
        'douYuXPath':douYuXPath,
        'douYuUrlHead':douYuUrlHead,

        'pandaUrl':pandaTiaoSanUrl,
        'pandaUrl1':pandaTiaoSanUrl1,
        'pandaXPath':pandaXPath,
        'pandaUrlHead':pandaUrlHead,

        'huyaUrl':huyaTiaoSanUrl,
        'huyaUrl1':huyaTiaoSanUrl1,
        'huyaXPath':huyaXPath,
        'huyaUrlHead':huyaUrlHead,

        'longzhuUrl':longzhuTiaoSanUrl,
        'longzhuUrl1':longzhuTiaoSanUrl1,
        'longzhuXPath':longzhuXPath,
        'longzhuUrlHead':longzhuUrlHead,

        'quanminUrl':quanminTiaoSanUrl,
        'quanminXPath':quanminXPath,
        'quanminUrlHead':quanminUrlHead,

        'huomaoUrl':'',
        'huomaoUrlHead':'',
        'huomaoJsonDir':'',

        'zhanqiUrl':zhanqiTiaoSanUrl,
        'zhanqiUrlHead':zhanqiUrlHead,
        'zhanqiJsonDir':zhanqiJsonDir,

        'index':9,
        'game':'TiaoSan',
                }


    dirs = {
        'dotaDirs':dotaDirs,
        'lolDirs':lolDirs,
        'dnfDirs':dnfDirs,
        'csDirs':csDirs,
        'howDirs':howDirs,
        'oWDirs':oWDirs,
        'meiNvDirs':meiNvDirs,
        'zhuJiDirs':zhuJiDirs,
        'tiaoSanDirs':tiaoSanDirs,
        }
    return dirs