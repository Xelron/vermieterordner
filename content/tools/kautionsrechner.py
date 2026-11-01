# -*- coding: utf-8 -*-
"""Kautionsrechner: Höchstbetrag (§ 551 Abs. 1 BGB) und Kautionszinsen (§ 551 Abs. 3 BGB).
Zinsberechnung identisch mit der Excel-Vorlage Kautionsabrechnung (Modus „berechnen“):
je Kalenderjahr taggenau, Zinsen am Jahresende dem Guthaben zugeschlagen, auf Cent gerundet."""
META = {
    "slug": "kautionsrechner",
    "name": "Kautionsrechner",
    "title": "Kautionsrechner: Höchstbetrag und Zinsen der Mietkaution",
    "description": "Höchstbetrag der Mietkaution (3 Nettokaltmieten) prüfen und die Kautionszinsen bis zur Rückzahlung berechnen – taggenau mit Zinseszins. Kostenlos.",
    "card_text": "Höchstbetrag prüfen und Zinsen bis zur Rückzahlung berechnen – taggenau mit Zinseszins.",
    "llms": "Rechner für die Mietkaution: Höchstbetrag 3 Nettokaltmieten (§ 551 Abs. 1 BGB) und Zinsen bis zur Rückzahlung (§ 551 Abs. 3 BGB), je Kalenderjahr taggenau mit jährlichem Zinseszins, wahlweise in drei Monatsraten gezahlt.",
    "date": "2026-11-01",
    "seo_title": "Kautionsrechner: Höchstbetrag & Kautionszinsen berechnen",
    "eyebrow": "Kostenloser Rechner · § 551 BGB",
    "answer": "Die Mietkaution darf **höchstens drei Monatsmieten ohne Betriebskosten** betragen. Der Vermieter muss sie verzinslich anlegen; die Zinsen gehören dem Mieter und erhöhen die Kaution (§ 551 BGB).",
    "order": 3,
    "faq": [
        ("Welchen Zinssatz soll ich eintragen?", "Wenn die Kaution auf einem Konto lag, zählen die tatsächlichen Zinsgutschriften laut Kontoauszug – dann brauchen Sie den Rechner für die Zinsen nicht. Für eine Schätzung oder wenn die Kaution nicht verzinslich angelegt war, nehmen Sie den üblichen Zins für Spareinlagen mit dreimonatiger Kündigungsfrist. Die Bundesbank weist für Einlagen mit vereinbarter Kündigungsfrist bis 3 Monate (vor allem von privaten Haushalten) zuletzt Werte um 0,7 % aus (August 2026: 0,73 %)."),
        ("Ich habe die Kaution auf meinem Girokonto gelassen. Muss ich trotzdem Zinsen zahlen?", "Die Kaution muss getrennt von Ihrem Vermögen bei einem Kreditinstitut zum üblichen Zins für Spareinlagen mit dreimonatiger Kündigungsfrist angelegt werden (§ 551 Abs. 3 BGB). Haben Sie das versäumt, schulden Sie dem Mieter nach verbreiteter Ansicht die entgangenen Zinsen als Schadensersatz. Rechnen Sie also mit dem üblichen Zins."),
        ("Darf der Mieter die Kaution in Raten zahlen?", "Ja. Bei einer Geldkaution darf der Mieter in drei gleichen monatlichen Teilzahlungen zahlen: die erste zu Beginn des Mietverhältnisses, die weiteren zusammen mit den beiden folgenden Mieten (§ 551 Abs. 2 BGB). Eine abweichende Vereinbarung zum Nachteil des Mieters ist unwirksam."),
        ("Wird meine Eingabe gespeichert?", "Nein. Der Rechner rechnet nur in Ihrem Browser, es wird nichts übertragen."),
    ],
    "sources": [
        ("§ 551 BGB – Begrenzung und Anlage von Mietsicherheiten (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bgb/__551.html"),
        ("Deutsche Bundesbank – Zinsstatistik, Einlagen mit vereinbarter Kündigungsfrist bis 3 Monate (PDF, Stand 01.10.2026)", "https://www.bundesbank.de/resource/blob/615016/ccfab4d2cd74209020e669db147fda6d/472B63F073F071307366337C94F8C870/s510atspar3-data.pdf"),
    ],
}

BODY = """<form class="calc" id="calc" onsubmit="return false">
<div class="row2">
<div><label for="kau">Kaution (€)</label><input type="text" id="kau" inputmode="decimal" value="1800" autocomplete="off"></div>
<div><label for="nkm">Nettokaltmiete (€/Monat, optional)</label><input type="text" id="nkm" inputmode="decimal" value="600" autocomplete="off"></div>
</div>
<div class="row2">
<div><label for="d1">Kaution gezahlt am (1. Rate)</label><input type="date" id="d1" value="2023-04-01"></div>
<div><label for="end">Abrechnung bzw. Rückzahlung am</label><input type="date" id="end" value="2026-11-30"></div>
</div>
<label class="chk"><input type="checkbox" id="raten" checked> In drei Monatsraten gezahlt</label>
<div class="row2">
<div><label for="zs">Zinssatz pro Jahr (%)</label><input type="text" id="zs" inputmode="decimal" value="0,7" autocomplete="off"></div>
<div></div>
</div>
<p class="hint">Bei Raten nimmt der Rechner drei gleiche Teilbeträge an (Rundungscent in der 3. Rate): am eingegebenen Tag, einen und zwei Monate später. Nettokaltmiete = Miete ohne Betriebskosten-Vorauszahlung oder -Pauschale.</p>
<div class="res" id="res" aria-live="polite"></div>
</form>"""

EXPLAIN = """<h2 class="serif" style="margin-top:0">So rechnet der Rechner</h2>
<p><strong>Höchstbetrag:</strong> Die Kaution darf höchstens das Dreifache der Monatsmiete ohne die als Pauschale oder Vorauszahlung ausgewiesenen Betriebskosten betragen (§ 551 Abs. 1 BGB). Ein Mehrbetrag ist unwirksam vereinbart (§ 551 Abs. 4 BGB).</p>
<p><strong>Zinsen:</strong> Für jedes Kalenderjahr rechnet der Rechner taggenau: Guthaben × Zinssatz × Tage ÷ Tage des Jahres (365 oder 366). Am Jahresende werden die Zinsen dem Guthaben zugeschlagen (Zinseszins) und auf den Cent gerundet. Eine Zahlung verzinst sich ab dem Tag nach dem Eingang; der Rückzahlungstag zählt mit. So rechnet auch unsere Excel-Vorlage im Modus „berechnen“.</p>
<p><strong>Ein Zinssatz für alle Jahre:</strong> Der Rechner nimmt denselben Satz für die ganze Zeit an. Lag die Kaution auf einem Konto, gelten die tatsächlichen Gutschriften laut Kontoauszug – das Ergebnis hier ist dann nur eine Schätzung.</p>
<p>Mehr dazu im Ratgeber <a href="kaution-zurueckzahlen.html">Kaution zurückzahlen: Fristen, Abzüge und Zinsen</a>.</p>
<p class="note">Allgemeine Information, keine Rechts- oder Steuerberatung. Im Einzelfall helfen Haus &amp; Grund, Mieterverein oder Anwalt.</p>"""

SCRIPT = r"""
function pd(v){if(!v)return null;var p=v.split('-');if(p.length!==3||!+p[0])return null;return Date.UTC(+p[0],+p[1]-1,+p[2])/864e5}
function ymd(t){var d=new Date(t*864e5);return [d.getUTCFullYear(),d.getUTCMonth(),d.getUTCDate()]}
function de(t){var a=ymd(t);return ('0'+a[2]).slice(-2)+'.'+('0'+(a[1]+1)).slice(-2)+'.'+a[0]}
function addm(t,n){var a=ymd(t),last=new Date(Date.UTC(a[0],a[1]+n+1,0)).getUTCDate();return Date.UTC(a[0],a[1]+n,Math.min(a[2],last))/864e5}
function r2(x){return Math.round((x+1e-9)*100)/100}
function calc(){var r=$('res'),k=num($('kau').value),m=num($('nkm').value),d1=pd($('d1').value),e=pd($('end').value),z=num($('zs').value),out='';
 if(k===null||k<=0){r.innerHTML=light('y','Bitte die Höhe der Kaution eingeben.');return}
 if(m!==null&&m>0){var h=r2(3*m);
  out+=k>h+0.005?light('r','Die Kaution übersteigt drei Nettokaltmieten ('+eur(h)+') um '+eur(r2(k-h))+'.','Dieser Teil ist unwirksam vereinbart (§ 551 Abs. 4 BGB); der Mieter kann ihn zurückverlangen.')
   :light('g','Höchstbetrag eingehalten: höchstens '+eur(h)+' (3 × '+eur(m)+').')}
 if(d1===null||e===null){r.innerHTML=out+light('y','Für die Zinsen bitte Zahlungsdatum und Rückzahlungsdatum eingeben.');return}
 if(z===null){r.innerHTML=out+light('y','Bitte einen Zinssatz eingeben, z. B. 0,7.');return}
 if(z<0){r.innerHTML=out+light('y','Der Zinssatz darf nicht negativ sein.');return}
 if(z>20){r.innerHTML=out+light('y','Bitte den Zinssatz in Prozent eingeben, z. B. 0,7 für 0,7 %.');return}
 var pays=[];if($('raten').checked){var t1=Math.floor(k/3*100+1e-9)/100;pays=[[d1,t1],[addm(d1,1),t1],[addm(d1,2),r2(k-2*t1)]]}else pays=[ [d1,r2(k)] ];
 if(e<d1){r.innerHTML=out+light('y','Das Rückzahlungsdatum liegt vor der Zahlung – bitte die Daten prüfen.');return}
 var y0=ymd(d1)[0],y1=ymd(e)[0];
 if(y1-y0>60){r.innerHTML=out+light('y','Mehr als 60 Jahre – bitte die Daten prüfen.');return}
 var late=pays.filter(function(p){return p[0]>e}).length;
 var carry=0,rows='',sumz=0,i=z/100;
 for(var y=y0;y<=y1;y++){var ys=Date.UTC(y,0,1)/864e5,ye=Date.UTC(y,11,31)/864e5,ep=Math.min(ye,e),ein=0,w=0;
  pays.forEach(function(p){if(p[0]>=ys&&p[0]<=ep){ein+=p[1];w+=p[1]*(ep-p[0])}});
  var zi=r2(i*(carry*(ep-ys+1)+w)/(ye-ys+1));carry=r2(carry+ein+zi);sumz=r2(sumz+zi);
  rows+='<tr><td>'+y+(ep<ye?'<br><small>bis '+de(ep)+'</small>':'')+(ein?'<br><small>+ '+eur(r2(ein))+' eingezahlt</small>':'')+'</td><td style="white-space:nowrap">'+eur(zi)+'</td><td style="white-space:nowrap">'+eur(carry)+'</td></tr>'}
 if(late)out+=light('y',(late===1?'Eine Rate liegt':'Raten liegen')+' nach dem Rückzahlungsdatum und '+(late===1?'wird':'werden')+' nicht berücksichtigt.');
 out+='<div class="kpis"><div class="kpi"><span>Zinsen</span><b>'+eur(sumz)+'</b></div><div class="kpi"><span>Kautionsguthaben</span><b>'+eur(carry)+'</b></div></div>';
 out+='<div class="tblwrap"><table class="tbl"><tr><th>Jahr</th><th>Zinsen</th><th>Stand</th></tr>'+rows+'</table></div>';
 out+='<p class="hint">Schätzung mit '+fmt(z,2)+' % in allen Jahren. Maßgeblich sind die tatsächlichen Zinsgutschriften der Bank.</p>';
 r.innerHTML=out}
['kau','nkm','d1','end','zs','raten'].forEach(function(i){$(i).addEventListener('input',calc);$(i).addEventListener('change',calc)});calc();
"""
