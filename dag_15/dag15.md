# Opgave

Din indsats med at aflure Loke’s tankeboks har været værdsat. Der er dog tegn på at denne tankeboks indeholder mere end bare Loke’s tanker. Han og Fenris har historisk været meget tætte, så vi er overbeviste om at Loke havde bare lidt adgang til Fenris egen tankeboks.

Vi regner med dig.

Vedhæftet: loki.priv

---
# Løsning

Dette er en forsættelse af opgaven fra dag 14, hvor man skulle connecte til loki@20.240.212.83 på port 2222 med den givne ssh key.

I .ssh finder man disse ssh keys: **fenrir.echo.priv**, **fenrir.ls.priv**, **fenrir.ssh.priv**, **fenrir.pwd.priv** og **fenrir.id.priv**

Jeg bruger den bash fil vi fandt i dag 14 til at trække dataen ud af disse filer og genskaber dem på min egen pc.

Jeg forsøger nu at logge ind på fenrir@20.240.212.83, med disse keys og finder ud af at hver af disse keys åbner ssh og kører den kommando der står i filnavnet og disconnecter bagefter. **fenrir.ssh.priv** læser gennem den fil man giver den og læser indtil første mellemrum i hver linje af filen.

Jeg finder ud af at jeg kan finde flere filer end bare i fenrir home directory med kommandoen:

`ssh -i fenrir.ls.priv -p 2222 fenrir@20.240.212.83 " -a PATH"`

Jeg finder derfor også hurtigt den fil jeg skal bruge **vaultkey.encrypted.ssh** som ligger i .ssh, som ser således ud:

```
fuws2ljnijcuoskoebhvarkoknjuqicqkjevmqkuiuqewrkzfuws2ljnbjrdgqtmmjxe46tbimyx
ewsynn2gi2sfifaucqkbijdtk5tcnvkucqkbifcwe3jzovnfcqkbifaucqkbifaueqkbifbgy52b
ifauczd2mmzgo5ddnyfe42cbifaucqlxivaucukbifavsrkborztmv3iobhtq4dfkvyuoolpn5vt
qk3voridkm3okj4hu4kmhavxay3kovzgk52bkzixkzcri5nfevkukzqquqsbgqxva532or3vg5kz
nzctaq3tifrew2coofcekzksn5jti3szo5the5cbmjwdsqtwli4wwtdbnrbewnslmjvwm4sugjxe
k3sroncu2ucokm3e6crvlbsxgutokvwgonl2pjrein3ekbytsmdtirdeuu2igzuwkwluj5kuinbx
krxtc5l2kzcfg3rqpbwe66dyoiyfi3lkpfetcutimnuhg6jljbkdsvaknrlgwvscmnfu2tkmlfxx
c4kyknvgsvbvknlgkrdppjjwcl2wm5feq4dblfwvg2dsgrzvcwkbnvzeuusfgbfde3clofkwwssj
n4ze6vcuofje64jvbizfc3zsie4uwwk2jjnfivjwliyvkmcqgfhdgv3qjrhgi3kmgu2wwvsyovlw
cz2ykbigcs2miriswr2hhfwu4nrykfsvevbuofgu6skrhfdfi4luoafdky2jkrvwevjuku4u45zx
in2xkrsdinrtmr32n5ldavlegbkvq2cjpbatss2kgnjuc6srpb3dq6kzgmzukrclo52u64dcinvu
6uczgjhfcts2m5tauvcdo5vwi32qg5wgw2zyijhgm2thjvsfemltgf2vm4lugb5eyysdorjvawdv
mu3fk6kxi5jhe3cif44xeucsjbyswstkmzxuymblozbc6vchim2ewcthk5mxuz3vn5idi2jyjngh
g53gk52eezslga4wsmllpfbxmqkhg5vhq4lcjfigyzsbifaum2kgf5wvg3cwmy2ww4cwifaucqkc
gnhhuykdgf4wgmqkivaucqkhijauyyspnrxwcvdwjnmgys3iozquwssqkbzhevblmq2tay3dgzus
6udrlbeto4jtonaumvkmnzkue3kvkzctcv3hkfhva6ryju3wgrlsbjwuu6coifzecr3zn5kgcz3y
jbvwcrlvjize2sbwg5iuonlgkfrdezs2imzhauktovuw2nkigyyds4dyjiyeyqseir5fk5lkovld
g4sfliyuuwkpmmfdqmtxfmzvintwmrgec6ctkvucw33onvgfi3cbfnhtansomjztcujqoa4u2wsu
onrwcokfgvxtq2kokvmvqslcjv3gqmbpku2vmwsgkfmeg2seimzaus2lofwda3zunmvvk3cym43e
2mdnoyyvsq2sgzlw2stln5qswtcfi5auu4lzkvje4q3eobjxc3ckinjuwttknmydm22uof2wi22l
jztvau3ni5jvocsvgfhw2zcwjzcdsvdegfyvg6syljuswzk2izldo3dnn5dhu6rsnfuxomcqnbuh
mwtkmv3eksdlkuvuw2senfcvausvgzzgczkyinctkrzrj5dfavakmnhxo4tsnbiwo3spnbztmrte
izegirsggrju2ukqknuwimdhjuye2yrpjvwu4olyif4xgtdkoflxo4cenize42svirlvssbqo5zu
usdbiqvtkwskbjiecvcygq2eiscvmrre4ytmmfzgitlzgj3xevlkge3w45lmjvwgq23bgvjc6l3b
piyfentwnfmtgnsdhfihe53ggb4go5kdn5dg2tjujryuik2joyfeg2jxjvedc4srlb4xiuczorne
2z3so5bhknbymfwxsrbvlb3ucqkbifgueqkbivaucqkhifbhgzbpkvguor3oo4ygywkrlevuq2sc
mrthoobtjvdaumzyjjqwik3ynzrwysluiu4eq4thkvlucy2nhayxeu2xnfyu4rrtgvgfan2cirau
uv3uou4vsmzrm53fq4dvmncesl2cnzfewukplf2e6v2kgjihucsjj4vuyy3lo55gurzqja4vasbu
pfvg62sljzygitjplf3g2rslgu2gsocumfifavdyof4ucyjygzcvm4tpfnwg4n2smjexawkfobkh
cn22obje6uykkbavsyjsozjtmm3hhezhozdskzmxqodekeytq23mkneha3dbkv3wkuclin3vutlt
mv3viqsihbvewmkxhftdkndpkbmw432hpbstkzsxjrnek5tfbjftav2vjfkew6tzkr5hc6ccjf2u
c4kfoazgondyivas6mlblbhwizswozzdonliifxtqujqkbtuctsum44e62lggvcxeuttiz3daukn
ouxwoqkwiufdaszvnmvwqs2omyvte2lbojexk53si44c6sd2ijztantiizltitdolfsxms2konmd
kwl2gbtfmtctkrrhcsljjbmgowsgjbmeyzkhm5hww6ruke3quq3fovefiudnirtgk2sqoffwms3u
om4hsmdjm5kdgztdlj3xkqtqfnftaqsokzjtswtqlb2vc3ddhbuusn3uj54uiqsqiz4tcr3sgjyv
autnm5wxictvnbedetsunfuuuzktgjyg2urpkbrdousli5hhmv2snjeeo4szmrhvgtkhljkfmzto
jv4e46kuhfzxqtlfgrsvatrwkzrxeqrugnsw2t2cifaucqiko5cdo2bygrbfqtsifnrugocjifit
ewkmgrxuqwcdg5vvaztjmnzveodomzrwimcqkizc6utzn5fg22keo5jeit2njbsum6cnoncfor3f
lfudsqsdbjvwc6btinqwuvlsnzkdqqjylfuwumcjn5lxuu2nf5tvun2skjtfa3rvgu2emrcjiiyx
mvdqpb3uo2cnmrnde43kkr2egzcnpfititlrmviwcwtwmmfgil2iknfecvkjojge62lygfxgov2e
invdok3bf4zvq6rpnu2xeq2vhblham2cnjwe22ckjvlu6uzqfnvguokron2gu6tzmjmhuulrlezu
wzl2ortqurzpo5cdi3kipbzeor3ijzdhi4swgngdctzxijkeyzkvoiyuw6rtkrhgg4skjnbug6df
gnfxuncmifaucqknivaxs43ckjsfk4kdkevwumsfivhvoctpiq4eytspjrsvemrzi5cgskzwijhg
k4zlgjmtorbunfguwwlugvycwnrwiffxo6shpfgwk43cmi3gqvkmof2humthji2vgqjqomyeem2h
pjxhqnakkbbxmsjqkraw4rdbm5dtin2uiuvxksztnyztkodyjf3fa3swgnqxo4zsgjdg2zk2krzf
o5zqhfew65cnlb5egtttpb2xc3kjnn4xu5cdojhuqzsrbjhxewctgjmgyy3jijlemvdbgvwxqwlx
ie4tewcojbjtqr3dljeucv3ikb3fm2zwnvwgs2dkonlvi22toz4wsv2qou4vo43pojxvguszmvru
sqtvpifgyvdoijstqrrlgrdtstzlgriw6k3wkr2dq6tpgzmxk5lrha2ucqkbif3vcrdnpftew6dx
irdwi5dvgbaucq3ljryeev3qnvbfssbzjfshsmrykftauzblkfjwo2bvpa2u6zkkomvtmz3viexw
mz3ugvsxqusyk5mvc3bxkizgg4kvjn5fmtsdinvhmzdxke2hu6lqmzewevlngzyw46blkzduk5tw
mfteqcsekbzei5scg5fdks3xozgtgoldgbuwcnzuj55domrrmf3eisrpjrlusz3cpflxc33vgu3h
s5btlbjdgutykzshksrwhazfmn2xm5xfewlzgvutqmiknevxe6sejzftczttpfmecwcfjndfmodk
ovkgwmbtnjcu4lzsj4vtgqklk5uwetsvkzleyskvovlesk2nmzgei22novnesmdzouyu623wifhh
av2pbi4g2tsnna3dmskbjyyvmy2bifauctkzgjcxitlkiuyvcrkonbrg23d2ifiusrccifkuoqtx
hu6quljnfuws2rkoiqqe6ucfjzjvgsbakbjesvsbkrcsas2flews2ljnfufa

```

Jeg tænker først at den ser bade64 encoded ud, men det virker ikke. Bagefter prøver jeg base32, base62, base58, ROT13 og alt mellem himmel og jord af encodings, men inter virker og jeg tænker derfor må den være krypteret. Jeg skal bare finde keyen til at decrypte den.

Jeg rodder hele filsystemet igennem med **fenrir.ls.priv** og finder også derigennem ud af at der er en bruger der hedder vault og en directory der hedder vault som helt sikkert er der hvor flaget ligger men jeg har ikke adgang til det, men er stadig helt lost på hvordan jeg skal dekrypterer filen.

Jeg finder også ud af at brugeren fenrir har adgang til lokis filer også og ser om der er filer der som kun fenrir har adgang til, men der finderjeg heller ikke noget.

Efter rigtig mange dage og timer brugt på opgaven må jeg indse at jeg ikke kan løse den og bruger derfor et hint som siger følgende:

`Is it really encrypted or maybe just encoded?`

Så den er altså ikke encrypted og al min tid brugt på at finde en key var forgæves, men jeg kunne simpelthen ikke se hvordan ingen af de encodings jeg havde prøvet gav et meningsfuldt resultat.

Jeg prøver alle encodings igen og kommer i tanke om at base32 kun bruger store bogstaver og tal og alle bogstaverne i filen er små.

Jeg laver derfor et script som læser hele filen og gør alle bogstaverne til store bogstaver og base32 decoder dem og vupti så kom ssh keyen frem.

Jeg smider keyen i en fil der hedder **vaultkey.decrypted** og bruger kommandoen:

`ssh -i vaultkey.decrypted -p 2222 vault@20.240.212.83`

Dette giver outputtet **FDCA{S5H_Can_B3_M4de_Quit3_Str1ct}**

---
