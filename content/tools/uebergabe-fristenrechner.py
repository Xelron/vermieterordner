# -*- coding: utf-8 -*-
"""Fristenrechner Wohnungsübergabe: Verjährung nach § 548 BGB (Auszug) und Frist für die
Wohnungsgeberbestätigung / Anmeldung (§§ 17, 19 BMG, Einzug).
Monatsfristen wie EDATE in der Excel-Vorlage Wohnungsübergabeprotokoll (§§ 187 Abs. 1, 188 Abs. 2, 3 BGB)."""
META = {
    "slug": "uebergabe-fristenrechner",
    "name": "Fristenrechner Wohnungsübergabe",
    "title": "Fristenrechner Wohnungsübergabe: Verjährung und Einzugsfrist",
    "description": "Wann verjähren Ersatzansprüche nach dem Auszug (§ 548 BGB)? Bis wann braucht der Mieter die Wohnungsgeberbestätigung? Kostenloser Rechner für Vermieter.",
    "card_text": "Auszug: Wann verjähren Ihre Ansprüche wegen Schäden? Einzug: Bis wann braucht der Mieter die Wohnungsgeberbestätigung?",
    "llms": "Rechner für Fristen bei der Wohnungsübergabe: Verjährung der Ersatzansprüche des Vermieters 6 Monate nach Rückgabe (§ 548 Abs. 1 BGB), Ansprüche des Mieters auf Aufwendungsersatz/Wegnahme 6 Monate nach Mietende (§ 548 Abs. 2 BGB), Anmeldung und Wohnungsgeberbestätigung binnen 2 Wochen nach Einzug (§ 17 Abs. 1, § 19 BMG).",
    "date": "2026-11-04",
    "seo_title": "Fristenrechner Wohnungsübergabe: § 548 BGB & Einzug",
    "eyebrow": "Kostenloser Rechner · § 548 BGB · § 19 BMG",
    "answer": "Ersatzansprüche des Vermieters wegen Schäden an der Wohnung verjähren **6 Monate nach der Rückgabe** (§ 548 Abs. 1 BGB). Beim Einzug muss der Mieter sich **innerhalb von 2 Wochen** anmelden – bis dahin braucht er Ihre Wohnungsgeberbestätigung (§§ 17, 19 BMG).",
    "order": 4,
    "faq": [
        ("Wann gilt die Wohnung als zurückgegeben?", "Wenn Sie die unmittelbare Sachherrschaft zurückerhalten haben und sich ungestört ein Bild vom Zustand machen können – in der Regel mit der Übergabe aller Schlüssel. Wirft der Mieter die Schlüssel nach einer gescheiterten Übergabe nur in den Briefkasten seiner bisherigen Wohnung, reicht das nicht (BGH, Urteil vom 12.10.2011, VIII ZR 8/11). Gehen Sie sicherheitshalber davon aus, dass die Frist läuft, sobald Sie die Schlüssel haben und in die Wohnung können. Gibt der Mieter vor dem Mietende zurück, beginnt die Frist schon mit der Rückgabe (BGH, Urteil vom 15.03.2006, VIII ZR 123/05)."),
        ("Stoppt das Übergabeprotokoll die Verjährung?", "Nein. Auch eine Mängelliste oder ein Schreiben an den Mieter hemmt die Verjährung nicht. Hemmend wirken zum Beispiel ein Mahnbescheid oder eine Klage (§ 204 BGB) und Verhandlungen mit dem Mieter über den Anspruch (§ 203 BGB)."),
        ("Was gilt, wenn das Fristende auf ein Wochenende fällt?", "Dann läuft die Frist erst am nächsten Werktag ab (§ 193 BGB, nach der Rechtsprechung auch für die Verjährung). Der Rechner zeigt das an, berücksichtigt aber keine Feiertage. Planen Sie trotzdem so, dass Sie vor dem rechnerischen Fristende handeln."),
        ("Was ist, wenn die 6 Monate schon vorbei sind?", "Dann kann der Mieter die Leistung verweigern. Gegen den Anspruch des Mieters auf Rückzahlung einer Barkaution dürfen Sie mit verjährten Schadensersatzforderungen in der Regel trotzdem noch aufrechnen – aber nur bis zu deren Höhe (BGH, Urteil vom 10.07.2024, VIII ZR 184/23)."),
        ("Wird meine Eingabe gespeichert?", "Nein. Der Rechner rechnet nur in Ihrem Browser, es wird nichts übertragen."),
    ],
    "sources": [
        ("§ 548 BGB – Verjährung der Ersatzansprüche und des Wegnahmerechts (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bgb/__548.html"),
        ("§ 188 BGB – Fristende (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bgb/__188.html"),
        ("§ 193 BGB – Sonn- und Feiertag; Sonnabend (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bgb/__193.html"),
        ("BGH, Urteil vom 15.03.2006, VIII ZR 123/05 – Verjährung ab Rückgabe vor Mietende (dejure.org)", "https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=15.03.2006&Aktenzeichen=VIII+ZR+123%2F05"),
        ("BGH, Urteil vom 12.10.2011, VIII ZR 8/11 – Rückgabe der Mietsache (dejure.org)", "https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=12.10.2011&Aktenzeichen=VIII+ZR+8%2F11"),
        ("§ 17 BMG – Anmeldung, Abmeldung (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bmg/__17.html"),
        ("§ 19 BMG – Mitwirkung des Wohnungsgebers (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bmg/__19.html"),
        ("BGH, Urteil vom 10.07.2024, VIII ZR 184/23 – Pressemitteilung Nr. 144/2024 (bundesgerichtshof.de)", "https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2024/2024144.html"),
    ],
}

BODY = """<form class="calc" id="calc" onsubmit="return false">
<label for="art">Anlass der Übergabe</label>
<select id="art"><option value="a" selected>Auszug</option><option value="e">Einzug</option></select>
<div class="row2" id="ra">
<div><label for="rueck">Rückgabe der Wohnung (Schlüssel­übergabe)</label><input type="date" id="rueck" value="2026-11-30" min="1990-01-01" max="2100-12-31"></div>
<div><label for="ende">Mietende laut Vertrag (optional)</label><input type="date" id="ende" value="" min="1990-01-01" max="2100-12-31"></div>
</div>
<p class="hint" id="ha">Zur Rückgabe: Maßgeblich ist der Tag, an dem Sie die Wohnung tatsächlich zurückerhalten – meist der Tag der Schlüsselübergabe.</p>
<div class="row2" id="re" hidden>
<div><label for="ein">Tag des Einzugs</label><input type="date" id="ein" value="2026-12-01" min="1990-01-01" max="2100-12-31"></div>
<div></div>
</div>
<p class="hint" id="he" hidden>Gemeint ist der tatsächliche Einzug des Mieters, nicht der Vertragsbeginn.</p>
<div class="res" id="res" aria-live="polite"></div>
</form>"""

EXPLAIN = """<h2 class="serif" style="margin-top:0">So rechnet der Rechner</h2>
<p><strong>Auszug:</strong> Ersatzansprüche des Vermieters wegen Veränderungen oder Verschlechterungen der Wohnung verjähren in sechs Monaten; die Frist beginnt, wenn Sie die Wohnung zurückerhalten (§ 548 Abs. 1 BGB). Der Rückgabetag zählt nicht mit, die Frist endet mit Ablauf des Tages im sechsten Monat, der dieselbe Zahl trägt – fehlt dieser Tag, am Monatsletzten (§§ 187, 188 BGB). Beispiel: Rückgabe 10.11.2026, Fristende 10.05.2027.</p>
<p><strong>Wochenende und Feiertage:</strong> Fällt das Fristende auf einen Samstag oder Sonntag, läuft die Frist erst am folgenden Montag ab (§ 193 BGB); der Rechner zeigt beide Daten. Feiertage berücksichtigt er nicht – fällt das Ende auf einen Feiertag, verschiebt es sich ebenfalls auf den nächsten Werktag. Planen Sie mit dem früheren Datum.</p>
<p><strong>Mietende (optional):</strong> Ansprüche des Mieters auf Ersatz von Aufwendungen oder auf Gestattung der Wegnahme einer Einrichtung verjähren sechs Monate nach der Beendigung des Mietverhältnisses (§ 548 Abs. 2 BGB).</p>
<p><strong>Einzug:</strong> Der Mieter muss sich innerhalb von zwei Wochen nach dem Einzug anmelden (§ 17 Abs. 1 BMG). Innerhalb dieser Frist müssen Sie ihm den Einzug schriftlich bestätigen oder ihn elektronisch gegenüber der Meldebehörde bestätigen (§ 19 Abs. 1 BMG). Der Rechner zählt 14 Tage ab dem Einzugstag.</p>
<p><strong>Ampel:</strong> Grün bei mehr als 8 Wochen Restzeit bis zum rechnerischen Fristende, Gelb bis 8 Wochen, Rot bei 14 Tagen oder weniger. Beim Einzug: Gelb bei 7 Tagen oder weniger, Rot bei 3 Tagen oder weniger.</p>
<p>Mehr dazu im Ratgeber <a href="uebergabeprotokoll-wohnung.html">Übergabeprotokoll Wohnung: Was rein muss</a>.</p>
<p class="note">Allgemeine Information, keine Rechtsberatung. Im Einzelfall helfen Haus &amp; Grund, Mieterverein oder Anwalt.</p>"""

SCRIPT = r"""
var WT=['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag'];
function pd(v){if(!v)return null;var p=v.split('-');if(p.length!==3||+p[0]<1990||+p[0]>2100)return null;return new Date(+p[0],+p[1]-1,+p[2])}
function de(d){return ('0'+d.getDate()).slice(-2)+'.'+('0'+(d.getMonth()+1)).slice(-2)+'.'+d.getFullYear()}
function dw(d){return WT[d.getDay()]+', '+de(d)}
function dm(d){return de(d)+' ('+WT[d.getDay()]+')'}
function edate(d,n){var t=new Date(d.getFullYear(),d.getMonth()+n,d.getDate());if(t.getDate()!==d.getDate())t=new Date(d.getFullYear(),d.getMonth()+n+1,0);return t}
function werktag(d){var w=d.getDay();return w===6?new Date(d.getFullYear(),d.getMonth(),d.getDate()+2):(w===0?new Date(d.getFullYear(),d.getMonth(),d.getDate()+1):d)}
function heute(){var h=new Date();h.setHours(0,0,0,0);return h}
function tg(a,b){return Math.round((b-a)/864e5)}
function nur(t){return t===0?'Heute ist der letzte Tag':'Nur noch '+rest(t)}
function rest(t){return t<0?'abgelaufen':(t===0?'heute letzter Tag':(t===1?'1 Tag':t+' Tage'))}
function calc(){var r=$('res'),a=$('art').value==='a',out='';
 $('ra').hidden=!a;$('ha').hidden=!a;$('re').hidden=a;$('he').hidden=a;
 if(a){var g=pd($('rueck').value),m=pd($('ende').value);
  if(!g){r.innerHTML=light('y',$('rueck').value?'Bitte ein Datum zwischen 1990 und 2100 eingeben.':'Bitte den Tag der Rückgabe eingeben.');return}
  var f=edate(g,6),fs=werktag(f),sh=fs>f,h=heute(),t=tg(h,f),tx=tg(h,fs);
  if(tx<0)out+=light('r','Die Verjährungsfrist ist mit Ablauf des '+de(fs)+' abgelaufen: Ersatzansprüche wegen Schäden kann der Mieter dann abwehren, wenn er sich auf die Verjährung beruft.','Gegen den Anspruch auf Rückzahlung einer Barkaution dürfen Sie in der Regel trotzdem noch aufrechnen – nur bis zur Höhe der Kaution (BGH VIII ZR 184/23). Feiertage berücksichtigt der Rechner nicht.');
  else if(t<0)out+=light('r','Das rechnerische Fristende ('+dw(f)+') ist vorbei. Weil es auf ein Wochenende fiel, läuft die Frist erst mit Ablauf des '+dm(fs)+' ab (§ 193 BGB).','Wenn Sie noch etwas unternehmen wollen (Mahnbescheid, Klage), dann sofort – und besser mit Beratung.');
  else if(t<=14)out+=light('r',nur(t)+(t===0?': Fristende am ':' bis zum Fristende am ')+dw(f)+(sh?' – nach § 193 BGB noch bis '+dw(fs):'')+'.','Reicht eine Barkaution nicht, rechtzeitig Mahnbescheid oder Klage – ein bloßes Schreiben an den Mieter hemmt nicht.');
  else if(t<=56)out+=light('y','Noch '+rest(t)+' bis zum Fristende am '+dw(f)+'.','Kautionsabrechnung jetzt fertigstellen und offene Schadensersatzforderungen klären.');
  else out+=light('g','Ersatzansprüche wegen Schäden verjähren 6 Monate nach der Rückgabe: Fristende am '+dw(f)+'.','Das Übergabeprotokoll allein stoppt die Frist nicht.');
  out+='<div class="kpis"><div class="kpi"><span>Fristende (§ 548 Abs. 1 BGB)</span><b>'+de(f)+'</b></div><div class="kpi"><span>Restzeit</span><b>'+(t<0&&tx>=0?(tx===0?'heute letzter Tag':rest(tx)):rest(t))+'</b></div></div>';
  if(sh&&t>=0)out+='<p class="hint">Der '+de(f)+' ist ein '+WT[f.getDay()]+'. Nach § 193 BGB läuft die Frist deshalb erst mit Ablauf des <strong>'+dm(fs)+'</strong> ab. Planen Sie trotzdem mit dem früheren Datum.</p>';
  if(m){var f2=edate(m,6);out+='<p class="hint">Mietende '+de(m)+': Ansprüche des Mieters auf Aufwendungsersatz oder Wegnahme von Einrichtungen verjähren 6 Monate nach dem Mietende, rechnerisch mit Ablauf des <strong>'+de(f2)+'</strong> (§ 548 Abs. 2 BGB).'+(g<m?' Die Rückgabe liegt vor dem Mietende – für Ihre Ersatzansprüche zählt trotzdem der Tag der Rückgabe.':'')+'</p>'}
  out+='<p class="hint">Rückgabe am '+de(g)+'. Eine feste Frist für die Kautionsabrechnung gibt es nicht – mehr dazu im Ratgeber <a href="kaution-zurueckzahlen.html">Kaution zurückzahlen</a>.</p>';
 }else{var e=pd($('ein').value);
  if(!e){r.innerHTML=light('y',$('ein').value?'Bitte ein Datum zwischen 1990 und 2100 eingeben.':'Bitte den Tag des Einzugs eingeben.');return}
  var w=new Date(e.getFullYear(),e.getMonth(),e.getDate()+14),t2=tg(heute(),w);
  if(t2<0)out+=light('r','Die Frist ist mit Ablauf des '+de(w)+' abgelaufen.','Stellen Sie die Wohnungsgeberbestätigung trotzdem sofort aus – der Mieter braucht sie für die Anmeldung.');
  else if(t2<=3)out+=light('r',nur(t2)+': Wohnungsgeberbestätigung bis '+dw(w)+'.','Stellen Sie die Bestätigung heute aus und geben Sie sie dem Mieter sofort.');
  else if(t2<=7)out+=light('y','Noch '+rest(t2)+': Wohnungsgeberbestätigung bis '+dw(w)+'.');
  else out+=light('g','Wohnungsgeberbestätigung und Anmeldung bis '+dw(w)+'.','Am einfachsten geben Sie die Bestätigung schon beim Übergabetermin mit.');
  out+='<div class="kpis"><div class="kpi"><span>Anmeldung und Bestätigung bis</span><b>'+de(w)+'</b></div><div class="kpi"><span>Restzeit</span><b>'+rest(t2)+'</b></div></div>';
  if(t2>=0&&(w.getDay()===0||w.getDay()===6))out+='<p class="hint">Der '+de(w)+' ist ein '+WT[w.getDay()]+' – geben Sie die Bestätigung am besten vorher.</p>';
  out+='<p class="hint">Einzug am '+de(e)+'. Die Bestätigung nennt Name und Anschrift des Wohnungsgebers (und ggf. des Eigentümers), das Einzugsdatum, die Anschrift der Wohnung und die Namen der meldepflichtigen Personen (§ 19 Abs. 3 BMG).</p>';
 }
 r.innerHTML=out}
if(location.hash==='#einzug')$('art').value='e';
['art','rueck','ende','ein'].forEach(function(i){$(i).addEventListener('input',calc);$(i).addEventListener('change',calc)});calc();
"""
