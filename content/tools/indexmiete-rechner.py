# -*- coding: utf-8 -*-
"""Indexmiete-Rechner: neue Nettokaltmiete nach § 557b BGB aus zwei Monatswerten des
Verbraucherpreisindex (VPI, 2020 = 100) und frühester Termin der neuen Miete.
Rechenweg wie in der Excel-Vorlage Mieterhöhung 2026 (Blatt Indexmiete):
neue Miete = ABRUNDEN(Miete × Index neu ÷ Index alt; 2);
Termin = MAX(Beginn des übernächsten Monats nach Zugang; erster Monatserster nach Ablauf eines Jahres
seit der letzten Mietänderung, §§ 187 Abs. 2, 188 Abs. 2, 3 BGB).
VPI-Werte: Destatis, Konjunkturindikatoren vpi001a (Stand 13.10.2026) – beim Nachtragen eines
neuen Monats VPI-Liste unten ergänzen und Stand in META/EXPLAIN anpassen."""

# VPI Deutschland, 2020 = 100, Monatswerte Jan 2021 – Sep 2026 (Destatis, Stand 13.10.2026)
VPI = {
    2021: [101.0, 101.6, 102.1, 102.4, 102.6, 102.9, 103.4, 103.5, 103.8, 104.3, 104.5, 104.7],
    2022: [105.2, 106.0, 108.1, 108.8, 109.8, 109.8, 110.3, 110.7, 112.7, 113.5, 113.7, 113.2],
    2023: [114.3, 115.2, 116.1, 116.6, 116.5, 116.8, 117.1, 117.5, 117.8, 117.8, 117.3, 117.4],
    2024: [117.6, 118.1, 118.6, 119.2, 119.3, 119.4, 119.8, 119.7, 119.7, 120.2, 119.9, 120.5],
    2025: [120.3, 120.8, 121.2, 121.7, 121.8, 121.8, 122.2, 122.3, 122.6, 123.0, 122.7, 122.7],
    2026: [122.8, 123.1, 124.5, 125.2, 125.0, 124.6, 125.6, 125.8, 126.6],
}
MON = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]


def _options(selected):
    out = ['<option value="">eigenen Wert eintragen</option>']
    for y in sorted(VPI, reverse=True):
        vals = VPI[y]
        for m in range(len(vals) - 1, -1, -1):
            v = f"{vals[m]:.1f}"
            key = f"{y}-{m + 1:02d}"
            sel = " selected" if key == selected else ""
            out.append(f'<option value="{v}" data-m="{MON[m]} {y}"{sel}>{MON[m]} {y}</option>')
    return "".join(out)


META = {
    "slug": "indexmiete-rechner",
    "name": "Indexmiete-Rechner",
    "title": "Indexmiete-Rechner: neue Miete nach dem Verbraucherpreisindex",
    "description": "Indexmiete berechnen: neue Nettokaltmiete aus dem Verbraucherpreisindex und frühester Termin nach § 557b BGB – VPI-Werte bis September 2026. Kostenlos.",
    "card_text": "Neue Miete aus zwei VPI-Monatswerten berechnen – mit Erhöhungsbetrag, Prozent und frühestem Termin nach § 557b BGB.",
    "llms": "Rechner für die Indexmiete (§ 557b BGB): neue Nettokaltmiete = bisherige Miete × VPI neu ÷ VPI alt (Monatswerte, Basis 2020 = 100, auf Cent abgerundet), VPI-Werte Januar 2021 bis September 2026 (Destatis, Stand 13.10.2026) zur Auswahl; neue Miete ab Beginn des übernächsten Monats nach Zugang der Erklärung, frühestens nach einem Jahr unveränderter Miete; vertragliche Mindeständerung optional.",
    "date": "2026-11-09",
    "seo_title": "Indexmiete-Rechner: neue Miete nach VPI berechnen",
    "eyebrow": "Kostenloser Rechner · § 557b BGB",
    "answer": "Bei einer Indexmiete ändert sich die Nettokaltmiete **im selben Verhältnis wie der Verbraucherpreisindex**: neue Miete = bisherige Miete × neuer Indexstand ÷ alter Indexstand. Die neue Miete gilt **ab Beginn des übernächsten Monats** nach Zugang Ihrer Erklärung – frühestens **ein Jahr nach der letzten Mietänderung** (§ 557b BGB).",
    "order": 6,
    "faq": [
        ("Welchen alten Indexstand nehme ich?", "Den Monatswert, auf dem Ihre jetzige Miete beruht: bei der ersten Anpassung der Monat, den der Mietvertrag als Ausgangspunkt nennt (oft der Monat des Vertragsschlusses oder Mietbeginns), danach der Monat, den Sie in der letzten Erhöhungserklärung als neuen Stand angegeben haben. Maßgeblich ist der Monatswert, nicht der Jahresdurchschnitt (BGH, Urteil vom 26.05.2021, VIII ZR 42/20)."),
        ("Mein Vertrag nennt einen Index mit Basis 2015 – was nun?", "Beide Werte müssen auf derselben Basis stehen. Nach der Rechtsprechung kommt es auf den Index an, der zum Zeitpunkt der Erhöhungserklärung gilt – derzeit Basis 2020 = 100 (BGH, VIII ZR 42/20). Nehmen Sie deshalb in der Regel auch den alten Monat in der Basis 2020 = 100; das Statistische Bundesamt rechnet frühere Monate auf diese Basis um."),
        ("Muss der Mieter der Erhöhung zustimmen?", "Nein. Bei einer wirksam vereinbarten Indexmiete genügt Ihre Erklärung in Textform (§ 557b Abs. 3 BGB). Der Mieter hat auch kein Sonderkündigungsrecht wie bei einer Erhöhung auf die Vergleichsmiete – § 561 BGB gilt nur für Erhöhungen nach §§ 558 und 559 BGB."),
        ("Was ist, wenn der Index gesunken ist?", "Dann kann der Mieter seinerseits verlangen, dass die Miete im selben Verhältnis sinkt – die Indexmiete wirkt in beide Richtungen. Eine Erhöhung ist dann nicht möglich."),
        ("Wird meine Eingabe gespeichert?", "Nein. Der Rechner rechnet nur in Ihrem Browser, es wird nichts übertragen."),
    ],
    "sources": [
        ("§ 557b BGB – Indexmiete (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bgb/__557b.html"),
        ("§ 188 BGB – Fristende (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bgb/__188.html"),
        ("Statistisches Bundesamt – Verbraucherpreisindex für Deutschland, Monatswerte 2020 = 100 (Stand 13.10.2026)", "https://www.destatis.de/DE/Themen/Wirtschaft/Konjunkturindikatoren/Basisdaten/vpi001a.html"),
        ("Statistisches Bundesamt – Verbraucherpreisindex (Themenseite mit aktuellen Werten)", "https://www.destatis.de/DE/Themen/Wirtschaft/Preise/Verbraucherpreisindex/_inhalt.html"),
        ("Statistisches Bundesamt – Pressemitteilung Nr. 364 vom 13.10.2026 (Inflationsrate September 2026 +3,3 %)", "https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/10/PD26_364_611.html"),
        ("BGH, Urteil vom 26.05.2021, VIII ZR 42/20 – Indexmiete: Monatsindex, Basisjahr, Wartefrist (iww.de)", "https://www.iww.de/mk/quellenmaterial/id/223308"),
        ("BGH, Urteil vom 22.11.2017, VIII ZR 291/16 – Erklärung ohne Prozentangabe wirksam (iww.de)", "https://www.iww.de/fmp/quellenmaterial/id/198625"),
    ],
}

BODY = f"""<form class="calc" id="calc" onsubmit="return false">
<div class="row2">
<div><label for="miete">Bisherige Nettokaltmiete (€/Monat)</label><input type="text" id="miete" inputmode="decimal" value="650" autocomplete="off"></div>
<div><label for="seit">Diese Miete gilt seit</label><input type="date" id="seit" value="2025-11-01" min="1990-01-01" max="2100-12-31"></div>
</div>
<div class="row2">
<div><label for="sa">Alter Indexstand (Monat)</label><select id="sa">{_options("2025-09")}</select></div>
<div><label for="ia">Alter Indexstand (Wert)</label><input type="text" id="ia" inputmode="decimal" value="122,6" autocomplete="off"></div>
</div>
<div class="row2">
<div><label for="sn">Neuer Indexstand (Monat)</label><select id="sn">{_options("2026-09")}</select></div>
<div><label for="in">Neuer Indexstand (Wert)</label><input type="text" id="in" inputmode="decimal" value="126,6" autocomplete="off"></div>
</div>
<div class="row2">
<div><label for="zug">Erklärung geht dem Mieter zu am</label><input type="date" id="zug" value="2026-11-10" min="1990-01-01" max="2100-12-31"></div>
<div><label for="mind">Mindeständerung laut Vertrag (%, optional)</label><input type="text" id="mind" inputmode="decimal" value="" autocomplete="off"></div>
</div>
<p class="hint">VPI für Deutschland, Basis 2020&nbsp;=&nbsp;100, Monatswerte des Statistischen Bundesamts bis September 2026 (Stand 13.10.2026). Für ältere oder neuere Monate den Wert selbst eintragen (aktuelle Werte beim Statistischen Bundesamt). Nennt Ihr Vertrag die Mindeständerung in Punkten, rechnen Sie sie in Prozent um. Nettokaltmiete = Miete ohne Betriebskosten.</p>
<div class="res" id="res" aria-live="polite"></div>
</form>"""

EXPLAIN = """<h2 class="serif" style="margin-top:0">So rechnet der Rechner</h2>
<p><strong>Neue Miete:</strong> bisherige Nettokaltmiete × neuer Indexstand ÷ alter Indexstand, auf den Cent abgerundet. Die Miete ändert sich also um den <em>Prozentsatz</em> der Indexänderung, nicht um die Punkte: von 120,0 auf 130,0 sind es 8,33&nbsp;%, nicht 10&nbsp;%. Die Abrundung ist eine vorsichtige Wahl – so verlangen Sie nie einen Cent zu viel.</p>
<p><strong>Ab wann:</strong> Die geänderte Miete ist ab Beginn des übernächsten Monats nach Zugang der Erklärung zu zahlen (§ 557b Abs. 3 BGB) – Zugang am 10.11. heißt neue Miete ab 01.01. Außerdem muss die Miete jeweils mindestens ein Jahr unverändert bleiben (§ 557b Abs. 2 BGB; Erhöhungen nach §§ 559 bis 560 BGB, etwa der Betriebskostenvorauszahlungen, zählen nicht mit). Der Rechner nimmt dafür den ersten Monatsersten, an dem seit „Diese Miete gilt seit“ ein volles Jahr vergangen ist.</p>
<p><strong>Vor Ablauf des Jahres zugestellt?</strong> Nach herrschender Meinung darf die Erklärung schon vorher zugehen; die neue Miete gilt dann frühestens ab dem ersten Monatsersten nach Ablauf des Jahres. Eine Entscheidung des BGH dazu gibt es nicht – wer ganz sicher gehen will, stellt erst nach Ablauf des Jahres zu.</p>
<p><strong>Mindeständerung:</strong> Manche Verträge erlauben eine Anpassung erst ab einer bestimmten Indexänderung, etwa 3&nbsp;%. Das ist eine Bagatellgrenze: Sie bestimmt, <em>ob</em> Sie anpassen dürfen, nicht, <em>wie viel</em> (BGH, VIII ZR 42/20). Ist sie nicht erreicht, zeigt der Rechner keine Erhöhung an.</p>
<p><strong>Nicht berücksichtigt:</strong> Feiertage, Staffel- oder Vergleichsmieterhöhungen und die geplante Deckelung der Indexmiete in angespannten Wohnungsmärkten (Gesetzentwurf, Stand 09.11.2026 noch nicht beschlossen – mehr im Ratgeber).</p>
<p>Mehr dazu im Ratgeber <a href="indexmiete-erhoehen.html">Indexmiete erhöhen: Berechnung, Erklärung und Fristen</a>.</p>
<p class="note">Allgemeine Information, keine Rechtsberatung. Im Einzelfall helfen Haus &amp; Grund, Mieterverein oder Anwalt.</p>"""

SCRIPT = r"""
var WT=['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag'];
function pd(v){if(!v)return null;var p=v.split('-');if(p.length!==3||+p[0]<1990||+p[0]>2100)return null;return new Date(+p[0],+p[1]-1,+p[2])}
function de(d){return ('0'+d.getDate()).slice(-2)+'.'+('0'+(d.getMonth()+1)).slice(-2)+'.'+d.getFullYear()}
function dm(d){return de(d)+' ('+WT[d.getDay()]+')'}
function jahr(d){var t=new Date(d.getFullYear()+1,d.getMonth(),d.getDate());if(t.getDate()!==d.getDate())t=new Date(d.getFullYear()+1,d.getMonth()+1,1);return t}
function erster(d){return d.getDate()===1?d:new Date(d.getFullYear(),d.getMonth()+1,1)}
function i10(x){return Math.round(x*10)}
function pc(x){return fmt(x,2).replace('-','−')+' %'}
function sync(s,i){var o=$(s).options[$(s).selectedIndex];if(o&&o.value)$(i).value=o.value.replace('.',',')}
function lab(s,i){var o=$(s).options[$(s).selectedIndex],v=num($(i).value);if(o&&o.value&&v!==null&&i10(v)===i10(+o.value))return o.getAttribute('data-m')+' ('+fmt(v,1)+')';return v===null?'':fmt(v,1)}
function calc(){var r=$('res'),m=num($('miete').value),a=num($('ia').value),n=num($('in').value),L=pd($('seit').value),Z=pd($('zug').value),mi=num($('mind').value),out='';
 if(m===null||m<=0){r.innerHTML=light('y','Bitte die bisherige Nettokaltmiete eingeben.');return}
 if(m>100000){r.innerHTML=light('y','Bitte die Monatsmiete in Euro eingeben.');return}
 if(Math.abs(m*100-Math.round(m*100))>1e-6){r.innerHTML=light('y','Bitte die Miete mit höchstens zwei Nachkommastellen eingeben.');return}
 if(a===null||n===null){r.innerHTML=light('y','Bitte den alten und den neuen Indexstand auswählen oder eintragen.');return}
 if(a<30||a>500||n<30||n>500){r.innerHTML=light('y','Die Indexstände sehen ungewöhnlich aus. Bitte Werte mit Basis 2020 = 100 eintragen (2026 etwa 123 bis 127).');return}
 var ac=i10(a),nc=i10(n),mc=Math.round(m*100);
 if(Math.abs(a*10-ac)>1e-6||Math.abs(n*10-nc)>1e-6){r.innerHTML=light('y','Bitte die Indexstände mit einer Nachkommastelle eintragen, so wie das Statistische Bundesamt sie veröffentlicht (z. B. 126,6).');return}
 if(($('seit').value&&!L)||($('zug').value&&!Z)){r.innerHTML=light('y','Bitte Daten zwischen 1990 und 2100 eingeben.');return}
 var p=(nc-ac)/ac*100,nk=Math.floor(mc*nc/ac),neu=nk/100,diff=(nk-mc)/100;
 var pk=fmt((nc-ac)/10,1);
 if(nc<ac){var s=Math.round(mc*nc/ac)/100;
  r.innerHTML=light('r','Der Index ist gesunken ('+pc(p)+'): keine Erhöhung möglich.','Der Mieter kann seinerseits verlangen, dass die Miete im selben Verhältnis sinkt – rechnerisch auf etwa '+eur(s)+'.');return}
 if(nc===ac){r.innerHTML=light('y','Der Index ist unverändert – keine Änderung der Miete.');return}
 if(nk===mc){r.innerHTML=light('y','Die Änderung beträgt weniger als 1 Cent – keine Erhöhung.');return}
 if(mi!==null&&mi>0&&(nc-ac)*10000<Math.round(mi*100)*ac){r.innerHTML=light('r','Keine Erhöhung möglich: Die Indexänderung von '+fmt(Math.floor((nc-ac)*10000/ac)/100,2)+' % erreicht die vertragliche Mindeständerung von '+fmt(mi,mi%1?2:0)+' % nicht.','Erst wenn die Schwelle erreicht ist, dürfen Sie die Anpassung verlangen – dann um die volle Änderung seit dem alten Indexstand (rechnerisch heute '+eur(neu)+').');return}
 out+='<div class="kpis"><div class="kpi"><span>Neue Nettokaltmiete</span><b>'+eur(neu)+'</b></div><div class="kpi"><span>Erhöhung pro Monat</span><b>'+eur(diff)+'</b></div></div>';
 out+='<p class="hint">Indexänderung: '+lab('sa','ia')+' → '+lab('sn','in')+' = +'+pk+' Punkte = +'+pc(p)+'. Mehreinnahme pro Jahr: '+eur((nk-mc)*12/100)+'.</p>';
 if(Z){var w1=new Date(Z.getFullYear(),Z.getMonth()+2,1),W=w1,J=null,wj=null;
  if(L){if(L>Z){out+=light('y','„Diese Miete gilt seit“ liegt nach dem Zugang – bitte die Daten prüfen.');r.innerHTML=out;return}
   J=jahr(L);wj=erster(J);if(wj>W)W=wj}
  if(L&&Z<J&&W>w1)out+=light('y','Neue Miete von '+eur(neu)+' frühestens ab '+de(W)+'.','Die Erklärung geht vor Ablauf des Jahres zu (Miete unverändert seit '+de(L)+', Jahr um ab '+de(J)+'). Das ist nach herrschender Meinung zulässig; die neue Miete gilt aber frühestens ab '+de(wj)+'. Ganz sicher gehen Sie, wenn Sie erst ab dem '+de(J)+' zustellen – dann gilt sie ab '+de(new Date(J.getFullYear(),J.getMonth()+2,1))+'.');
  else if(L&&Z<J)out+=light('g','Neue Miete von '+eur(neu)+' ab '+de(W)+'.','Die Erklärung geht vor Ablauf des Jahres zu (Miete unverändert seit '+de(L)+', Jahr um ab '+de(J)+'). Das ist nach herrschender Meinung zulässig; die Jahresfrist verschiebt den Termin hier nicht. Zugang am '+de(Z)+' → Beginn des übernächsten Monats.');
  else out+=light('g','Neue Miete von '+eur(neu)+' ab '+de(W)+'.',(L?'Die Jahresfrist ist eingehalten (Miete unverändert seit '+de(L)+'). ':'Ohne Datum „Diese Miete gilt seit“ prüft der Rechner die Jahresfrist nicht. ')+'Zugang am '+de(Z)+' → Beginn des übernächsten Monats.');
  if(W.getTime()===w1.getTime())out+='<p class="hint">Für eine Erhöhung ab '+de(w1)+' muss die Erklärung spätestens am '+de(new Date(w1.getFullYear(),w1.getMonth()-1,0))+' zugehen. Zugang nachweisbar machen, etwa durch Einwurf mit Zeugen oder Boten.</p>'}
 else out+=light('y','Für den Termin bitte das Datum eingeben, an dem die Erklärung dem Mieter zugeht.');
 out+='<p class="hint"><strong>In die Erklärung (Textform)</strong> gehören die eingetretene Indexänderung – alter und neuer Indexstand mit Monat – und die neue Miete oder der Erhöhungsbetrag in Euro (§ 557b Abs. 3 BGB). Empfehlenswert: den Termin der neuen Miete nennen. Die Prozentangabe ist nicht nötig, schadet aber nicht.</p>';
 r.innerHTML=out}
function unsel(s,i){var o=$(s).options[$(s).selectedIndex],v=num($(i).value);if(o&&o.value&&(v===null||i10(v)!==i10(+o.value)))$(s).selectedIndex=0}
$('sa').addEventListener('change',function(){sync('sa','ia');calc()});$('sn').addEventListener('change',function(){sync('sn','in');calc()});
$('ia').addEventListener('input',function(){unsel('sa','ia')});$('in').addEventListener('input',function(){unsel('sn','in')});
['miete','seit','ia','in','zug','mind'].forEach(function(i){$(i).addEventListener('input',calc);$(i).addEventListener('change',calc)});calc();
"""
