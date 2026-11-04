# -*- coding: utf-8 -*-
"""Gebäude-AfA-Rechner: lineare AfA für vermietete Gebäude im Privatvermögen (§ 7 Abs. 4 S. 1 Nr. 2 EStG),
im Anschaffungsjahr monatsgenau (§ 7 Abs. 1 S. 4 EStG), ohne Grund und Boden.
Rechenweg wie in der Excel-Vorlage Anlage V 2026 (Blatt AfA): Bemessungsgrundlage = (Kaufpreis + Nebenkosten) × (1 − Anteil Grund und Boden),
Satz nach Fertigstellungsjahr, Kaufjahr × (13 − Anschaffungsmonat) / 12. Zusätzlich Rechenhilfe 15-%-Grenze (§ 6 Abs. 1 Nr. 1a EStG)."""
META = {
    "slug": "gebaeude-afa-rechner",
    "name": "Gebäude-AfA-Rechner",
    "title": "Gebäude-AfA-Rechner: Abschreibung für vermietete Immobilien",
    "description": "AfA für vermietete Häuser und Wohnungen berechnen: Gebäudeanteil ohne Grund und Boden, 2 %, 2,5 % oder 3 % je nach Baujahr, im Kaufjahr monatsgenau.",
    "card_text": "Kaufpreis und Nebenkosten ohne Grund und Boden, Satz nach Fertigstellungsjahr, AfA im Kaufjahr monatsgenau – mit 15-%-Grenze.",
    "llms": "Rechner für die lineare Gebäude-AfA im Privatvermögen: Bemessungsgrundlage aus Kaufpreis plus Kaufnebenkosten ohne Anteil Grund und Boden, Satz 3 % (fertiggestellt ab 2023), 2 % (1925–2022), 2,5 % (vor 1925) nach § 7 Abs. 4 S. 1 Nr. 2 EStG, im Kaufjahr monatsgenau (§ 7 Abs. 1 S. 4 EStG), optional selbst genutzter Flächenanteil, Rechenhilfe 15-%-Grenze für anschaffungsnahe Herstellungskosten (§ 6 Abs. 1 Nr. 1a EStG).",
    "date": "2026-11-04",
    "seo_title": "AfA-Rechner Immobilie: Gebäude-AfA 2 %, 2,5 %, 3 % berechnen",
    "eyebrow": "Kostenloser Rechner · § 7 EStG",
    "answer": "Vermieter schreiben das **Gebäude** ab, nicht den Grund und Boden: jährlich **2 %** (fertiggestellt 1925 bis 2022), **2,5 %** (vor 1925) oder **3 %** (ab 2023) von Kaufpreis plus Nebenkosten ohne Bodenanteil. Im Kaufjahr zählt die AfA **ab dem Monat der Anschaffung** (§ 7 EStG).",
    "order": 5,
    "faq": [
        ("Woher weiß ich den Anteil für Grund und Boden?", "Steht im Kaufvertrag eine Aufteilung, ist sie grundsätzlich maßgeblich, solange sie die realen Wertverhältnisse nicht grundsätzlich verfehlt und wirtschaftlich haltbar ist (BFH, Urteil vom 21.07.2020, IX R 26/19). Fehlt sie, wird nach den Verkehrswerten von Boden und Gebäude aufgeteilt. Eine erste Orientierung gibt der Bodenrichtwert × Grundstücksfläche (bei Eigentumswohnungen Ihr Miteigentumsanteil). Das Finanzamt nutzt oft die Arbeitshilfe des Bundesfinanzministeriums zur Kaufpreisaufteilung – sie ist laut BFH aber nicht bindend. Geplant ist eine gesetzliche Regelung: Nach dem Regierungsentwurf zum Jahressteuergesetz 2026 (§ 6f EStG-E, Kabinettsbeschluss vom 12.08.2026) könnte das Ergebnis der Arbeitshilfe zugrunde gelegt und eine Abweichung nur mit dem Gutachten eines öffentlich bestellten und vereidigten Sachverständigen oder einer nach DIN EN ISO/IEC 17024 zertifizierten Person nachgewiesen werden – nach dem Entwurf erst für Kaufverträge, die nach der Verkündung geschlossen werden. Das Gesetz ist noch nicht in Kraft."),
        ("Zählt das Baujahr oder das Kaufjahr?", "Für den Satz zählt das Jahr, in dem das Gebäude fertiggestellt wurde – meist das Baujahr. Ein 1968 gebautes Haus, das Sie 2024 kaufen, schreiben Sie mit 2 % ab. Das Kaufjahr bestimmt nur, ab wann die AfA läuft."),
        ("Kann ich schneller abschreiben?", "Ist die tatsächliche Nutzungsdauer kürzer als 50 Jahre (bei 2 %), 40 Jahre (2,5 %) bzw. 33 Jahre (3 %), dürfen Sie nach der kürzeren Dauer abschreiben – das müssen Sie nachweisen, etwa mit einem Gutachten (§ 7 Abs. 4 S. 2 EStG). Für neu gebaute Wohngebäude kommen unter engen Voraussetzungen die degressive AfA (§ 7 Abs. 5a EStG) oder die Sonderabschreibung nach § 7b EStG in Betracht. Beides rechnet dieser Rechner nicht."),
        ("Was ist mit Renovierungskosten nach dem Kauf?", "Instandsetzung und Modernisierung in den ersten drei Jahren nach dem Kauf sind Herstellungskosten, wenn sie ohne Umsatzsteuer 15 % der Anschaffungskosten des Gebäudes übersteigen (§ 6 Abs. 1 Nr. 1a EStG). Dann erhöhen sie die AfA-Bemessungsgrundlage, statt sofort abziehbar zu sein. Der Rechner zeigt die Grenze als Rechenhilfe; mehr dazu im Ratgeber zur Anlage V."),
        ("Wird meine Eingabe gespeichert?", "Nein. Der Rechner rechnet nur in Ihrem Browser, es wird nichts übertragen."),
    ],
    "sources": [
        ("§ 7 EStG – Absetzung für Abnutzung (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/estg/__7.html"),
        ("§ 6 EStG – Bewertung, Abs. 1 Nr. 1a anschaffungsnahe Herstellungskosten (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/estg/__6.html"),
        ("§ 9 EStG – Werbungskosten, Abs. 1 S. 3 Nr. 7 AfA (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/estg/__9.html"),
        ("BMF-Schreiben vom 26.01.2026, IV C 1 - S 2253/00082/001/064 – Instandsetzung und Modernisierung von Gebäuden (PDF, via ivd.net)", "https://ivd.net/wp-content/uploads/2026/02/2026-01-26-instandsetzung-modernisierung-gebaeude-1.pdf"),
        ("Der Betrieb, 26.08.2026 – Kaufpreisaufteilung: gesetzliche Neuregelung durch das JStG 2026 (§ 6f EStG-E)", "https://der-betrieb.de/meldungen/kaufpreisaufteilung-bei-bebauten-grundstuecken-gesetzliche-neuregelung-durch-das-jahressteuergesetz-2026-%c2%a7-6f-estg-e/"),
        ("BFH, Urteil vom 21.07.2020, IX R 26/19 – Kaufpreisaufteilung auf Grund und Gebäude (dejure.org)", "https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BFH&Datum=21.07.2020&Aktenzeichen=IX+R+26%2F19"),
    ],
}

BODY = """<form class="calc" id="calc" onsubmit="return false">
<div class="row2">
<div><label for="kp">Kaufpreis (€)</label><input type="text" id="kp" inputmode="decimal" value="400.000" autocomplete="off"></div>
<div><label for="nk">Kaufnebenkosten (€)</label><input type="text" id="nk" inputmode="decimal" value="36.100" autocomplete="off"></div>
</div>
<p class="hint">Nebenkosten: Grunderwerbsteuer, Notar und Grundbuch für den Eigentumsübergang, Makler. Nicht dazu: Kosten für die Grundschuld (sofort abziehbar).</p>
<div class="row2">
<div><label for="gb">Anteil Grund und Boden (%)</label><input type="text" id="gb" inputmode="decimal" value="25" autocomplete="off"></div>
<div><label for="bj">Fertigstellungsjahr (Baujahr)</label><input type="text" id="bj" inputmode="numeric" value="1968" autocomplete="off"></div>
</div>
<div class="row2">
<div><label for="dat">Übergang von Besitz, Nutzen und Lasten</label><input type="date" id="dat" value="2024-07-01" min="1950-01-01" max="2100-12-31"></div>
<div><label for="eig">Selbst genutzter Anteil der Wohnfläche (%, optional)</label><input type="text" id="eig" inputmode="decimal" value="" placeholder="0" autocomplete="off"></div>
</div>
<p class="hint">Maßgeblich für den Beginn der AfA ist der Übergang laut Kaufvertrag, nicht der Notartermin. Den selbst genutzten oder unentgeltlich überlassenen Anteil tragen Sie nur ein, wenn Sie einen Teil des Hauses nicht vermieten.</p>
<div id="live" aria-live="polite"></div>
<div class="res" id="res"></div>
</form>"""

EXPLAIN = """<h2 class="serif" style="margin-top:0">So rechnet der Rechner</h2>
<p><strong>Bemessungsgrundlage:</strong> Kaufpreis plus Kaufnebenkosten, abzüglich des Anteils für Grund und Boden. Grund und Boden nutzt sich nicht ab und wird nicht abgeschrieben.</p>
<p><strong>AfA-Satz</strong> nach dem Fertigstellungsjahr (§ 7 Abs. 4 S. 1 Nr. 2 EStG): fertiggestellt nach dem 31.12.2022 jährlich 3 %, vom 01.01.1925 bis 31.12.2022 jährlich 2 %, vor dem 01.01.1925 jährlich 2,5 %.</p>
<p><strong>Kaufjahr:</strong> Die Jahres-AfA vermindert sich um ein Zwölftel für jeden vollen Monat vor dem Monat der Anschaffung (§ 7 Abs. 1 S. 4 EStG). Bei Übergang im Juli zählen also 6/12, im Dezember 1/12. Danach gilt jedes Jahr die volle AfA, bis das Gebäude vollständig abgeschrieben ist.</p>
<p><strong>Eigennutzung:</strong> Wohnen Sie selbst im Haus, rechnet der Rechner den vermieteten Anteil vereinfacht nach Wohnfläche. Nur die AfA auf diesen Anteil ist Werbungskosten.</p>
<p><strong>Nicht abgebildet:</strong> nachträgliche Herstellungskosten, kürzere Nutzungsdauer per Gutachten, degressive AfA (§ 7 Abs. 5a EStG), Sonderabschreibung (§ 7b EStG), Gebäude im Betriebsvermögen, Erbschaft und Schenkung (dort führen Sie die AfA des Vorgängers fort).</p>
<p>Mehr dazu im Ratgeber <a href="anlage-v-vermietung.html#afa">Anlage V ausfüllen: Mieteinnahmen und Werbungskosten</a>. Die <a href="anlage-v.html">Excel-Vorlage Anlage V 2026</a> rechnet die AfA genauso und übernimmt sie in die Summen für die Steuererklärung.</p>"""

SCRIPT = r"""
var MON=['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'];
function eu(n){return eur(n).replace(' €','&nbsp;€')}
function eu2(c){return eu(c/100)}
function pc(n){return n.toLocaleString('de-DE',{maximumFractionDigits:2})+'&nbsp;%'}
function pn(v){v=(v||'').replace(/\s|€|%/g,'');if(!v)return null;if(!/^[\d.,]+$/.test(v)||!/\d/.test(v))return NaN;var n=num(v);return n===null?NaN:n}
function calc(){var L=$('live'),r=$('res'),kp=pn($('kp').value),nk=pn($('nk').value),gb=pn($('gb').value),eig=pn($('eig').value),bjs=($('bj').value||'').trim(),bj=/^\d{4}$/.test(bjs)?+bjs:null,dv=$('dat').value,out='';
 function err(h,s){L.innerHTML=light('y',h,s);r.innerHTML=''}
 if(kp===null)return err('Bitte den Kaufpreis eingeben.');
 if(isNaN(kp))return err('Bitte den Kaufpreis als Zahl eingeben, z. B. 400.000 oder 400000.');
 if(nk!==null&&isNaN(nk))return err('Bitte die Kaufnebenkosten als Zahl eingeben (oder leer lassen).');
 if(nk===null)nk=0;
 if(gb===null||isNaN(gb)||gb<0||gb>=100)return err('Bitte den Anteil für Grund und Boden in Prozent eingeben (0 bis unter 100), z. B. 25.');
 if(eig!==null&&isNaN(eig))return err('Bitte den selbst genutzten Anteil als Zahl eingeben (oder leer lassen).');
 if(eig===null)eig=0;
 if(eig<0||eig>100)return err('Der selbst genutzte Anteil muss zwischen 0 und 100&nbsp;% liegen.');
 if(bj===null||bj<1500||bj>2100)return err('Bitte das Fertigstellungsjahr vierstellig eingeben, z. B. 1968.');
 var p=dv.split('-');if(p.length!==3||+p[0]<1950||+p[0]>2100)return err('Bitte das Datum des Übergangs eingeben (zwischen 1950 und 2100).');
 var ky=+p[0],km=+p[1];
 if(bj>ky)return err('Das Fertigstellungsjahr liegt nach dem Kaufjahr – bitte prüfen.','Beim Kauf vom Bauträger vor Fertigstellung oder beim eigenen Neubau beginnt die AfA erst mit der Fertigstellung. Diesen Fall rechnet der Rechner nicht.');
 // Beträge in Cent; Rundung wie in der Excel-Vorlage: ROUND(BMG × Satz × Monate/12; 2)
 var akC=Math.round((kp+nk)*100),gebC=Math.round(akC*(100-gb)/100);
 if(gebC<10000)return err('Die AfA-Bemessungsgrundlage (Gebäudeanteil) liegt unter 100&nbsp;€ – bitte Kaufpreis und Anteil für Grund und Boden prüfen.');
 var satz=bj>=2023?3:(bj>=1925?2:2.5),txt=bj>=2023?'fertiggestellt nach dem 31.12.2022':(bj>=1925?'fertiggestellt 1925 bis 2022':'fertiggestellt vor 1925');
 var mon=13-km,vollC=Math.round(gebC*satz/100),erstC=Math.round(gebC*satz*mon/1200);
 var restC=gebC-erstC,n=Math.ceil(restC/vollC),endj=ky+n,lastC=restC-(n-1)*vollC;
 var ant=(100-eig)/100,mitEig=eig>0&&eig<100,vm=function(c){return Math.round(c*ant)};
 var kaufTxt=km===12?'Dezember':MON[km-1]+' bis Dezember';
 if(eig>=100)L.innerHTML=light('r','Bei 100&nbsp;% Eigennutzung gibt es keine AfA als Werbungskosten.','Die AfA ist nur für vermietete Gebäude(teile) abziehbar. Die Werte unten zeigen die rechnerische AfA für das ganze Gebäude.');
 else L.innerHTML=light('g','AfA-Satz '+pc(satz)+' ('+txt+'): '+eu2(vollC)+' im vollen Jahr.','Im Kaufjahr '+ky+' ab '+MON[km-1]+': '+mon+'/12 = '+eu2(erstC)+'.'+(mitEig?' Davon vermietet ('+pc(100-eig)+'): '+eu2(vm(vollC))+' im vollen Jahr, '+eu2(vm(erstC))+' im Kaufjahr.':''));
 out+='<div class="kpis"><div class="kpi"><span>AfA-Bemessungsgrundlage</span><b>'+eu2(gebC)+'</b></div><div class="kpi"><span>AfA-Satz</span><b>'+pc(satz)+'</b></div></div>';
 out+='<div class="kpis"><div class="kpi"><span>AfA '+ky+' ('+mon+'/12)</span><b>'+eu2(erstC)+'</b></div><div class="kpi"><span>AfA ab '+(ky+1)+' pro Jahr</span><b>'+eu2(vollC)+'</b></div></div>';
 var td=function(a,b,c){return '<tr><td>'+a+'</td><td style="white-space:nowrap">'+b+(mitEig&&c!==undefined?'<br><small>vermietet: '+c+'</small>':'')+'</td></tr>'};
 var rows=td('Kaufpreis + Nebenkosten',eu2(akC))+td('− Grund und Boden ('+pc(gb)+')',eu2(akC-gebC))+td('<strong>= Gebäude (Bemessungs&shy;grundlage)</strong>','<strong>'+eu2(gebC)+'</strong>',mitEig?eu2(vm(gebC)):undefined);
 rows+=td('AfA '+ky+' ('+kaufTxt+')',eu2(erstC),mitEig?eu2(vm(erstC)):undefined);
 if(n>1)rows+=td('AfA '+(ky+1)+(endj-1>ky+1?' bis '+(endj-1):'')+' je Jahr',eu2(vollC),mitEig?eu2(vm(vollC)):undefined);
 if(n>0)rows+=td((lastC<vollC?'Rest ':'Letzte AfA ')+endj+' (voll abge&shy;schrieben)',eu2(lastC),mitEig?eu2(vm(lastC)):undefined);
 out+='<div class="tblwrap"><table class="tbl"><tr><th scope="col">Rechenweg</th><th scope="col">Betrag'+(mitEig?'<br><small>davon vermietet ('+pc(100-eig)+')</small>':'')+'</th></tr>'+rows+'</table></div>';
 if(mitEig)out+='<p class="hint">Im Formular (so in der Anlage V 2025) steht die Gebäude-AfA dann in der Spalte „verhältnismäßige Zuordnung“: Gesamtbetrag (im Kaufjahr '+eu2(erstC)+', danach '+eu2(vollC)+') und abzugsfähiger Anteil '+pc(100-eig)+'. Der vermietete Anteil ist hier vereinfacht nach Wohnfläche gerechnet.</p>';
 if(bj>=2023)out+='<p class="hint">Für neu gebaute Wohngebäude kommen unter engen Voraussetzungen auch die degressive AfA (§ 7 Abs. 5a EStG) oder die Sonderabschreibung nach § 7b EStG in Betracht. Diese rechnet der Rechner nicht – lassen Sie sich beraten.</p>';
 if(eig>=100){r.innerHTML=out;return}
 var basC=mitEig?vm(gebC):gebC,gC=Math.round(basC*0.15);
 out+='<h3 style="margin-top:22px">Rechenhilfe: 15-%-Grenze nach dem Kauf</h3>';
 out+='<p class="hint">Instandsetzung und Modernisierung, die innerhalb von drei Jahren nach dem Übergang am '+p[2]+'.'+p[1]+'.'+p[0]+' durchgeführt werden, sind Herstellungskosten, wenn sie <strong>ohne Umsatzsteuer</strong> 15&nbsp;% der Anschaffungskosten des Gebäudes übersteigen (§ 6 Abs. 1 Nr. 1a EStG). '
  +(mitEig?'Bei teilweiser Eigennutzung wird die Grenze je Gebäudeteil geprüft. Vereinfacht nach Wohnfläche entfallen auf den vermieteten Teil '+eu2(basC)+' Anschaffungskosten; die Grenze dafür liegt bei <strong>'+eu2(gC)+' netto</strong> – verglichen mit den Kosten, die auf den vermieteten Teil entfallen.':'Grenze hier: 15&nbsp;% von '+eu2(gebC)+' = <strong>'+eu2(gC)+' netto</strong>.')
  +' Bei Rechnungen mit durchgehend 19&nbsp;% Umsatzsteuer entspricht das '+eu2(Math.round(gC*1.19))+' brutto.</p>';
 out+='<p class="hint">Schönheitsreparaturen zählen mit, jährlich übliche Arbeiten wie Wartung nicht. Wird die Grenze überschritten, sind alle diese Kosten nicht sofort abziehbar, sondern erhöhen die AfA – auch rückwirkend für Vorjahre. Nur eine Rechenhilfe: Ob eine Maßnahme dazugehört, wie bei mehreren Gebäudeteilen aufzuteilen ist und wann die Frist genau endet, klären Sie im Zweifel mit Ihrer Steuerberatung.</p>';
 r.innerHTML=out}
['kp','nk','gb','bj','dat','eig'].forEach(function(i){$(i).addEventListener('input',calc);$(i).addEventListener('change',calc)});calc();
"""
