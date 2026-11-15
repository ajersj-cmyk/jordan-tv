D='dec/smali_classes2/tv/jordan/app/'
M=D+'MainActivity.smali'; B=D+'MainActivity$Bridge.smali'
m=open(M).read(); b=open(B).read()
def rep(s,old,new,count=1):
    n=s.count(old); assert n==count,(n,old[:100]); return s.replace(old,new)
MA='Ltv/jordan/app/MainActivity;'
# fields + helpers
m=rep(m,'.field private webView:Landroid/webkit/WebView;','''.field private webView:Landroid/webkit/WebView;

.field public volatile wantedFile:Ljava/lang/String;

.field public lastArrowAt:J

.field public static archiveExec:Ljava/util/concurrent/ExecutorService;

.field public static metaCache:Ljava/util/concurrent/ConcurrentHashMap;''')
helpers=f'''
.method public static jtExec()Ljava/util/concurrent/ExecutorService;
    .locals 1
    sget-object v0, {MA}->archiveExec:Ljava/util/concurrent/ExecutorService;
    if-nez v0, :jt_have
    invoke-static {{}}, Ljava/util/concurrent/Executors;->newSingleThreadExecutor()Ljava/util/concurrent/ExecutorService;
    move-result-object v0
    sput-object v0, {MA}->archiveExec:Ljava/util/concurrent/ExecutorService;
    :jt_have
    return-object v0
.end method

.method public static jtStale({MA}Ljava/lang/String;)Z
    .locals 1
    iget-object v0, p0, {MA}->wantedFile:Ljava/lang/String;
    if-eqz v0, :jt_fresh
    invoke-virtual {{v0, p1}}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-nez v0, :jt_fresh
    const/4 v0, 0x1
    return v0
    :jt_fresh
    const/4 v0, 0x0
    return v0
.end method

.method private jtMeta(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .locals 2
    sget-object v0, {MA}->metaCache:Ljava/util/concurrent/ConcurrentHashMap;
    if-nez v0, :jt_map
    new-instance v0, Ljava/util/concurrent/ConcurrentHashMap;
    invoke-direct {{v0}}, Ljava/util/concurrent/ConcurrentHashMap;-><init>()V
    sput-object v0, {MA}->metaCache:Ljava/util/concurrent/ConcurrentHashMap;
    :jt_map
    invoke-virtual {{v0, p1}}, Ljava/util/concurrent/ConcurrentHashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;
    move-result-object v1
    if-eqz v1, :jt_miss
    check-cast v1, Ljava/lang/String;
    return-object v1
    :jt_miss
    invoke-direct {{p0, p1, p2, p3, p4}}, {MA}->request(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v1
    if-eqz v1, :jt_out
    invoke-virtual {{v1}}, Ljava/lang/String;->isEmpty()Z
    move-result v0
    if-nez v0, :jt_out
    sget-object v0, {MA}->metaCache:Ljava/util/concurrent/ConcurrentHashMap;
    invoke-virtual {{v0}}, Ljava/util/concurrent/ConcurrentHashMap;->size()I
    move-result p2
    const/16 p3, 0xc
    if-lt p2, p3, :jt_put
    invoke-virtual {{v0}}, Ljava/util/concurrent/ConcurrentHashMap;->clear()V
    :jt_put
    invoke-virtual {{v0, p1, v1}}, Ljava/util/concurrent/ConcurrentHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    :jt_out
    return-object v1
.end method
'''
m=m.rstrip('\n')+'\n'+helpers
# metadata request -> cached
m=rep(m,'''    const-string v11, "{}"

    invoke-direct {v1, v14, v15, v11, v3}, Ltv/jordan/app/MainActivity;->request(''','''    const-string v11, "{}"

    invoke-direct {v1, v14, v15, v11, v3}, Ltv/jordan/app/MainActivity;->jtMeta(''')
# key repeat throttle
start=m.index('.method public dispatchKeyEvent(Landroid/view/KeyEvent;)Z')
end=m.index('.end method',start)
seg=m[start:end]
seg=rep(seg,'.method public dispatchKeyEvent(Landroid/view/KeyEvent;)Z\n    .locals 9','.method public dispatchKeyEvent(Landroid/view/KeyEvent;)Z\n    .locals 11')
seg=rep(seg,'''    :cond_18
    iget-object v5, p0, Ltv/jordan/app/MainActivity;->webView:Landroid/webkit/WebView;''',f'''    :cond_18
    invoke-virtual {{p1}}, Landroid/view/KeyEvent;->getRepeatCount()I
    move-result v5
    if-eqz v5, :jt_send
    invoke-virtual {{p1}}, Landroid/view/KeyEvent;->getEventTime()J
    move-result-wide v5
    iget-wide v7, p0, {MA}->lastArrowAt:J
    sub-long v7, v5, v7
    const-wide/16 v9, 0xb4
    cmp-long v7, v7, v9
    if-gez v7, :jt_keep
    return v3
    :jt_keep
    iput-wide v5, p0, {MA}->lastArrowAt:J
    :jt_send
    iget-object v5, p0, Ltv/jordan/app/MainActivity;->webView:Landroid/webkit/WebView;''')
m=m[:start]+seg+m[end:]
open(M,'w').write(m)

T='Ltv/jordan/app/MainActivity$Bridge;->this$0:Ltv/jordan/app/MainActivity;'
def method(s,sig):
    a=s.index(sig); e=s.index('.end method',a); return a,e
def patch_method(sig,fn):
    global b
    a,e=method(b,sig); b=b[:a]+fn(b[a:e])+b[e:]
def stale_check(param):
    def f(seg):
        head,rest=seg.split('\n',1)
        # insert after .locals line
        i=rest.index('\n',rest.index('.locals'))+1
        ins=f'''    iget-object v0, p0, {T}
    invoke-static {{v0, {param}}}, {MA}->jtStale({MA}Ljava/lang/String;)Z
    move-result v0
    if-eqz v0, :jt_go
    return-void
    :jt_go
'''
        return head+'\n'+rest[:i]+ins+rest[i:]
    return f
patch_method('.method private synthetic lambda$playFile$31(',stale_check('p3'))
patch_method('.method private synthetic lambda$playFile$32(',stale_check('p2'))
patch_method('.method private synthetic lambda$playAmbient$24(',stale_check('p3'))
patch_method('.method private synthetic lambda$playAmbient$25(',stale_check('p2'))
def set_wanted(expr_reg_code):
    def f(seg):
        head,rest=seg.split('\n',1)
        # after annotation end if present, else after .locals
        anchor='.end annotation\n' if '.end annotation\n' in rest else None
        i=(rest.index(anchor)+len(anchor)) if anchor else rest.index('\n',rest.index('.locals'))+1
        return head+'\n'+rest[:i]+expr_reg_code+rest[i:]
    return f
setp1=f'''    iget-object v0, p0, {T}
    iput-object p1, v0, {MA}->wantedFile:Ljava/lang/String;
'''
patch_method('.method public playFile(Ljava/lang/String;Ljava/lang/String;IIIII)V',set_wanted(setp1))
patch_method('.method public playAmbient(Ljava/lang/String;Ljava/lang/String;)V',set_wanted(setp1))
patch_method('.method public playFull(Ljava/lang/String;Ljava/lang/String;I)V',set_wanted(setp1))
patch_method('.method public hidePlayer()V',set_wanted(f'''    iget-object v0, p0, {T}
    const-string v1, ""
    iput-object v1, v0, {MA}->wantedFile:Ljava/lang/String;
'''))
# hidePlayer lambda: pause -> stop
patch_method('.method private synthetic lambda$hidePlayer$11()V',lambda s: rep(s,'invoke-interface {v0}, Landroidx/media3/exoplayer/ExoPlayer;->pause()V','invoke-interface {v0}, Landroidx/media3/exoplayer/ExoPlayer;->stop()V'))
# threads -> single executor (playFile, playAmbient)
def to_exec(reg_t,reg_r,lam):
    def f(seg):
        seg=rep(seg,f'    new-instance {reg_t}, Ljava/lang/Thread;\n\n','')
        seg=rep(seg,f'    invoke-direct {{{reg_t}, {reg_r}}}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V\n','')
        seg=rep(seg,f'    invoke-virtual {{{reg_t}}}, Ljava/lang/Thread;->start()V',f'''    invoke-static {{}}, {MA}->jtExec()Ljava/util/concurrent/ExecutorService;
    move-result-object {reg_t}
    invoke-interface {{{reg_t}, {reg_r}}}, Ljava/util/concurrent/ExecutorService;->execute(Ljava/lang/Runnable;)V''')
        return seg
    return f
patch_method('.method public playFile(Ljava/lang/String;Ljava/lang/String;IIIII)V',to_exec('v0','v1','29'))
patch_method('.method public playAmbient(Ljava/lang/String;Ljava/lang/String;)V',to_exec('v2','v3','20'))
open(B,'w').write(b)
print('smali ok')
