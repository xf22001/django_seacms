# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SeaAdmin(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    logincount = models.SmallIntegerField()
    loginip = models.CharField(max_length=16)
    logintime = models.IntegerField()
    groupid = models.SmallIntegerField()
    state = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sea_admin'


class SeaArcrank(models.Model):
    id = models.SmallAutoField(primary_key=True)
    rank = models.SmallIntegerField()
    membername = models.CharField(max_length=20)
    adminrank = models.SmallIntegerField()
    money = models.PositiveSmallIntegerField()
    scores = models.IntegerField()
    purviews = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_arcrank'


class SeaBuy(models.Model):
    uid = models.IntegerField()
    vid = models.IntegerField()
    kptime = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sea_buy'


class SeaCck(models.Model):
    ckey = models.CharField(max_length=80)
    climit = models.IntegerField()
    maketime = models.DateTimeField(blank=True, null=True)
    usetime = models.DateTimeField(blank=True, null=True)
    uname = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'sea_cck'


class SeaCoCls(models.Model):
    clsname = models.CharField(max_length=50)
    sysclsid = models.PositiveSmallIntegerField()
    cotype = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sea_co_cls'


class SeaCoConfig(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)
    getlistnum = models.IntegerField()
    getconnum = models.IntegerField()
    cotype = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sea_co_config'


class SeaCoData(models.Model):
    v_id = models.AutoField(primary_key=True)
    tid = models.PositiveSmallIntegerField()
    tname = models.CharField(max_length=60)
    v_name = models.CharField(max_length=60)
    v_state = models.PositiveIntegerField()
    v_pic = models.CharField(max_length=255)
    v_spic = models.CharField(max_length=255)
    v_gpic = models.CharField(max_length=255)
    v_hit = models.PositiveIntegerField()
    v_money = models.SmallIntegerField()
    v_rank = models.SmallIntegerField()
    v_digg = models.SmallIntegerField()
    v_tread = models.SmallIntegerField()
    v_commend = models.SmallIntegerField()
    v_wrong = models.PositiveSmallIntegerField()
    v_director = models.CharField(max_length=200)
    v_enname = models.CharField(max_length=200)
    v_lang = models.CharField(max_length=200)
    v_actor = models.CharField(max_length=200)
    v_color = models.CharField(max_length=7)
    v_publishyear = models.CharField(max_length=20)
    v_publisharea = models.CharField(max_length=20)
    v_addtime = models.PositiveIntegerField()
    v_topic = models.PositiveIntegerField()
    v_note = models.CharField(max_length=30)
    v_tags = models.CharField(max_length=30)
    v_letter = models.CharField(max_length=3)
    v_from = models.CharField(max_length=255)
    v_inbase = models.CharField(max_length=1)
    v_des = models.TextField(blank=True, null=True)
    v_playdata = models.TextField(blank=True, null=True)
    v_downdata = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_co_data'


class SeaCoFilters(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    rcolumn = models.IntegerField(db_column='rColumn')  # Field name made lowercase.
    uesmode = models.IntegerField(db_column='uesMode')  # Field name made lowercase.
    sfind = models.CharField(db_column='sFind', max_length=255)  # Field name made lowercase.
    sstart = models.CharField(db_column='sStart', max_length=255)  # Field name made lowercase.
    send = models.CharField(db_column='sEnd', max_length=255)  # Field name made lowercase.
    sreplace = models.CharField(db_column='sReplace', max_length=255)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.
    cotype = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sea_co_filters'


class SeaCoNews(models.Model):
    n_id = models.AutoField(primary_key=True)
    tid = models.PositiveSmallIntegerField()
    n_title = models.CharField(max_length=60)
    n_keyword = models.CharField(max_length=80, blank=True, null=True)
    n_pic = models.CharField(max_length=255)
    n_hit = models.PositiveIntegerField()
    n_author = models.CharField(max_length=80, blank=True, null=True)
    n_addtime = models.IntegerField()
    n_letter = models.CharField(max_length=3)
    n_content = models.TextField(blank=True, null=True)
    n_outline = models.CharField(max_length=255, blank=True, null=True)
    tname = models.CharField(max_length=60)
    n_from = models.CharField(max_length=50)
    n_inbase = models.CharField(max_length=1)
    n_entitle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_co_news'


class SeaCoType(models.Model):
    tid = models.AutoField(primary_key=True)
    cid = models.PositiveSmallIntegerField()
    tname = models.CharField(max_length=50)
    siteurl = models.CharField(max_length=200)
    getherday = models.PositiveSmallIntegerField()
    playfrom = models.CharField(max_length=50)
    autocls = models.CharField(max_length=1)
    classid = models.PositiveSmallIntegerField()
    coding = models.CharField(max_length=10)
    sock = models.CharField(max_length=1)
    addtime = models.PositiveIntegerField()
    cjtime = models.PositiveIntegerField()
    listconfig = models.TextField(blank=True, null=True)
    itemconfig = models.TextField(blank=True, null=True)
    isok = models.PositiveIntegerField()
    cotype = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sea_co_type'


class SeaCoUrl(models.Model):
    uid = models.AutoField(primary_key=True)
    cid = models.PositiveSmallIntegerField()
    tid = models.PositiveSmallIntegerField()
    url = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)
    succ = models.CharField(max_length=1)
    err = models.IntegerField()
    cotype = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sea_co_url'


class SeaComment(models.Model):
    uid = models.PositiveIntegerField()
    v_id = models.PositiveIntegerField()
    typeid = models.PositiveSmallIntegerField()
    username = models.CharField(max_length=20)
    ip = models.CharField(max_length=15)
    ischeck = models.SmallIntegerField()
    dtime = models.PositiveIntegerField()
    msg = models.TextField(blank=True, null=True)
    m_type = models.PositiveIntegerField()
    reply = models.PositiveIntegerField()
    agree = models.PositiveIntegerField()
    anti = models.PositiveIntegerField()
    pic = models.CharField(max_length=255)
    vote = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'sea_comment'


class SeaContent(models.Model):
    v_id = models.IntegerField(primary_key=True)
    tid = models.PositiveSmallIntegerField()
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_content'


class SeaCount(models.Model):
    userip = models.CharField(max_length=16, blank=True, null=True)
    serverurl = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_count'


class SeaCrons(models.Model):
    cronid = models.SmallAutoField(primary_key=True)
    available = models.IntegerField()
    type = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    filename = models.CharField(max_length=255)
    lastrun = models.PositiveIntegerField()
    nextrun = models.PositiveIntegerField()
    weekday = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    minute = models.CharField(max_length=36)

    class Meta:
        managed = True
        db_table = 'sea_crons'


class SeaData(models.Model):
    v_id = models.AutoField(primary_key=True)
    tid = models.PositiveSmallIntegerField()
    v_name = models.CharField(max_length=60)
    v_state = models.PositiveIntegerField()
    v_pic = models.CharField(max_length=255)
    v_spic = models.CharField(max_length=255)
    v_gpic = models.CharField(max_length=255)
    v_hit = models.PositiveIntegerField()
    v_money = models.SmallIntegerField()
    v_rank = models.SmallIntegerField()
    v_digg = models.SmallIntegerField()
    v_tread = models.SmallIntegerField()
    v_commend = models.SmallIntegerField()
    v_wrong = models.PositiveSmallIntegerField()
    v_ismake = models.PositiveSmallIntegerField()
    v_actor = models.CharField(max_length=200, blank=True, null=True)
    v_color = models.CharField(max_length=7)
    v_publishyear = models.IntegerField(blank=True, null=True)
    v_publisharea = models.CharField(max_length=20)
    v_addtime = models.PositiveIntegerField()
    v_topic = models.PositiveIntegerField()
    v_note = models.CharField(max_length=30)
    v_tags = models.CharField(max_length=30)
    v_letter = models.CharField(max_length=3)
    v_isunion = models.SmallIntegerField()
    v_recycled = models.SmallIntegerField()
    v_director = models.CharField(max_length=200, blank=True, null=True)
    v_enname = models.CharField(max_length=200, blank=True, null=True)
    v_lang = models.CharField(max_length=200, blank=True, null=True)
    v_score = models.IntegerField(blank=True, null=True)
    v_scorenum = models.IntegerField(blank=True, null=True)
    v_extratype = models.TextField(blank=True, null=True)
    v_jq = models.TextField(blank=True, null=True)
    v_nickname = models.CharField(max_length=60, blank=True, null=True)
    v_reweek = models.CharField(max_length=60, blank=True, null=True)
    v_douban = models.FloatField(blank=True, null=True)
    v_mtime = models.FloatField(blank=True, null=True)
    v_imdb = models.FloatField(blank=True, null=True)
    v_tvs = models.CharField(max_length=60, blank=True, null=True)
    v_company = models.CharField(max_length=60, blank=True, null=True)
    v_dayhit = models.IntegerField(blank=True, null=True)
    v_weekhit = models.IntegerField(blank=True, null=True)
    v_monthhit = models.IntegerField(blank=True, null=True)
    v_daytime = models.IntegerField(blank=True, null=True)
    v_weektime = models.IntegerField(blank=True, null=True)
    v_monthtime = models.IntegerField(blank=True, null=True)
    v_len = models.CharField(max_length=6, blank=True, null=True)
    v_total = models.CharField(max_length=6, blank=True, null=True)
    v_ver = models.CharField(max_length=20, blank=True, null=True)
    v_psd = models.CharField(max_length=30, blank=True, null=True)
    v_longtxt = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_data'


class SeaErradd(models.Model):
    id = models.AutoField(primary_key=True)
    vid = models.PositiveIntegerField()
    author = models.CharField(max_length=60)
    ip = models.CharField(max_length=15)
    errtxt = models.TextField(blank=True, null=True)
    sendtime = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'sea_erradd'


class SeaFavorite(models.Model):
    uid = models.IntegerField()
    vid = models.IntegerField()
    kptime = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sea_favorite'


class SeaFlink(models.Model):
    id = models.SmallAutoField(primary_key=True)
    sortrank = models.SmallIntegerField()
    url = models.CharField(max_length=60)
    webname = models.CharField(max_length=30)
    msg = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    logo = models.CharField(max_length=60)
    dtime = models.PositiveIntegerField()
    ischeck = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'sea_flink'


class SeaGuestbook(models.Model):
    uid = models.PositiveIntegerField()
    title = models.CharField(max_length=60)
    mid = models.PositiveIntegerField(blank=True, null=True)
    posttime = models.PositiveIntegerField()
    uname = models.CharField(max_length=30)
    ip = models.CharField(max_length=20)
    dtime = models.PositiveIntegerField()
    ischeck = models.SmallIntegerField()
    msg = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_guestbook'


class SeaIe(models.Model):
    ip = models.CharField(max_length=15)
    addtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_ie'


class SeaJqtype(models.Model):
    tid = models.SmallAutoField(primary_key=True)
    upid = models.SmallIntegerField()
    tname = models.CharField(max_length=30)
    ishidden = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'sea_jqtype'


class SeaMember(models.Model):
    username = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=255)
    logincount = models.SmallIntegerField()
    regip = models.CharField(max_length=16)
    regtime = models.IntegerField()
    gid = models.SmallIntegerField()
    points = models.IntegerField()
    state = models.SmallIntegerField()
    stime = models.IntegerField()
    vipendtime = models.CharField(max_length=15)
    acode = models.CharField(max_length=35)
    repswcode = models.CharField(max_length=35)
    msgbody = models.TextField(blank=True, null=True)
    msgstate = models.CharField(max_length=2)

    class Meta:
        managed = True
        db_table = 'sea_member'


class SeaMemberGroup(models.Model):
    gid = models.AutoField(primary_key=True)
    gname = models.CharField(max_length=32)
    gtype = models.CharField(max_length=255)
    g_auth = models.CharField(max_length=32)
    g_upgrade = models.IntegerField()
    g_authvalue = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sea_member_group'


class SeaMyad(models.Model):
    aid = models.AutoField(primary_key=True)
    adname = models.CharField(max_length=100)
    adenname = models.CharField(max_length=60)
    timeset = models.PositiveIntegerField()
    intro = models.CharField(max_length=255)
    adsbody = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_myad'


class SeaMytag(models.Model):
    aid = models.AutoField(primary_key=True)
    tagname = models.CharField(max_length=30)
    tagdes = models.CharField(max_length=50)
    addtime = models.PositiveIntegerField()
    tagcontent = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_mytag'


class SeaNews(models.Model):
    n_id = models.AutoField(primary_key=True)
    tid = models.PositiveSmallIntegerField()
    n_title = models.CharField(max_length=255)
    n_pic = models.CharField(max_length=255)
    n_hit = models.PositiveIntegerField()
    n_money = models.SmallIntegerField()
    n_rank = models.SmallIntegerField()
    n_digg = models.SmallIntegerField()
    n_tread = models.SmallIntegerField()
    n_commend = models.SmallIntegerField()
    n_author = models.CharField(max_length=80, blank=True, null=True)
    n_color = models.CharField(max_length=7)
    n_addtime = models.PositiveIntegerField()
    n_note = models.SmallIntegerField()
    n_letter = models.CharField(max_length=3)
    n_isunion = models.SmallIntegerField()
    n_recycled = models.SmallIntegerField()
    n_entitle = models.CharField(max_length=200, blank=True, null=True)
    n_outline = models.CharField(max_length=255, blank=True, null=True)
    n_keyword = models.CharField(max_length=80, blank=True, null=True)
    n_from = models.CharField(max_length=50, blank=True, null=True)
    n_score = models.BigIntegerField(blank=True, null=True)
    n_scorenum = models.IntegerField(blank=True, null=True)
    n_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_news'


class SeaPlaydata(models.Model):
    v_id = models.IntegerField(primary_key=True)
    tid = models.PositiveSmallIntegerField()
    body = models.TextField(blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_playdata'


class SeaSearchKeywords(models.Model):
    aid = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=30)
    spwords = models.CharField(max_length=50)
    count = models.PositiveIntegerField()
    result = models.PositiveIntegerField()
    lasttime = models.PositiveIntegerField()
    tid = models.PositiveSmallIntegerField()

    class Meta:
        managed = True
        db_table = 'sea_search_keywords'


class SeaTags(models.Model):
    tagid = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30)
    usenum = models.PositiveIntegerField()
    vids = models.TextField()

    class Meta:
        managed = True
        db_table = 'sea_tags'


class SeaTemp(models.Model):
    v_id = models.AutoField(primary_key=True)
    tid = models.PositiveSmallIntegerField()
    v_name = models.CharField(max_length=60)
    v_state = models.PositiveIntegerField()
    v_pic = models.CharField(max_length=100)
    v_actor = models.CharField(max_length=200, blank=True, null=True)
    v_publishyear = models.CharField(max_length=20)
    v_publisharea = models.CharField(max_length=20)
    v_addtime = models.PositiveIntegerField()
    v_note = models.CharField(max_length=30)
    v_letter = models.CharField(max_length=3)
    v_playdata = models.TextField(blank=True, null=True)
    v_des = models.TextField(blank=True, null=True)
    v_director = models.CharField(max_length=200, blank=True, null=True)
    v_enname = models.CharField(max_length=200, blank=True, null=True)
    v_lang = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_temp'


class SeaTopic(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    enname = models.CharField(max_length=60)
    sort = models.IntegerField()
    template = models.CharField(max_length=50)
    pic = models.CharField(max_length=80)
    des = models.TextField(blank=True, null=True)
    vod = models.TextField()
    keyword = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sea_topic'


class SeaType(models.Model):
    tid = models.SmallAutoField(primary_key=True)
    upid = models.PositiveIntegerField()
    tname = models.CharField(max_length=30)
    tenname = models.CharField(max_length=60)
    torder = models.IntegerField()
    templist = models.CharField(max_length=50)
    templist_1 = models.CharField(max_length=50)
    templist_2 = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    keyword = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    ishidden = models.SmallIntegerField()
    unionid = models.TextField(blank=True, null=True)
    tptype = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'sea_type'


class SeaZyk(models.Model):
    zid = models.AutoField(primary_key=True)
    zname = models.CharField(max_length=60)
    zapi = models.CharField(max_length=255)
    zinfo = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'sea_zyk'
