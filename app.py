"use client";
import { useState, useEffect } from "react";

export default function Page() {
  const [news, setNews] = useState<any[]>([
    {title:"Euro-area Inflation: Headline pressures rise - Nordea", date:"10/2/2026", pair:"EUR/USD", bias:"Bullish"},
    {title:"Euro trims daily gains as Eurozone inflation accelerates above expectations", date:"10/2/2026", pair:"EUR/USD", bias:"Bearish"},
    {title:"US pressures EU to tap emergency diesel stockpiles", date:"10/2/2026", pair:"EUR/USD", bias:"Bearish"},
  ]);

  // LIVE NEWS - free, no API key
  useEffect(()=>{
    fetch("https://api.rss2json.com/v1/api.json?rss_url=https://www.forexlive.com/feed/")
   .then(r=>r.json()).then(d=>{
      if(d.items){
        const mapped = d.items.slice(0,5).map((i:any)=>({
          title: i.title,
          date: new Date(i.pubDate).toLocaleDateString(),
          pair: i.title.includes("EUR")?"EUR/USD": i.title.includes("GBP")?"GBP/USD":"EUR/USD",
          bias: i.title.toLowerCase().includes("dollar") && i.title.toLowerCase().includes("high")? "Bearish" : "Bullish"
        }));
        setNews(mapped);
      }
    }).catch(()=>{});
  },[]);

  const bearish = 57.1; const bullish = 42.9;

  return (
    <div className="min-h-screen bg-[#F7F8FA] p-4">
      <div className="max-w-[420px] mx-auto">
        <div className="flex justify-between items-center py-3 mb-2">
          <div className="font-black text-[#0B3D3D] text-xl">TRADER<br/>SENTIMENTS.</div>
          <div className="flex gap-2"><div className="w-10 h-10 bg-white rounded-xl border flex items-center justify-center">🛒</div><div className="w-10 h-10 bg-white rounded-xl border flex items-center justify-center">👤</div></div>
        </div>

        {/* GAUGE CARD - EXACT LIKE YOUR SCREENSHOT */}
        <div className="bg-black rounded-[24px] p-6 mb-4 text-white text-center">
          <h2 className="text-2xl font-bold">EUR/USD Sentiment</h2><h2 className="text-3xl font-bold mb-4">Gauge</h2>
          <div className="relative w-64 h-32 mx-auto overflow-hidden">
            <div className="absolute w-64 h-64 rounded-full border-[16px] border-[#1A1A1A]" style={{borderTopColor:"#0B84FF", borderRightColor:"#A3D9C9", borderLeftColor:"#0B84FF", borderBottomColor:"transparent", transform:"rotate(-40deg)"}}></div>
            <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-1 h-16 bg-white origin-bottom" style={{transform:`translateX(-50%) rotate(${bearish-50}deg)`}}></div>
            <div className="absolute bottom-2 left-1/2 -translate-x-1/2 text-xs text-[#888]">Bearish</div>
          </div>
          <div className="flex justify-between mt-4 px-4">
            <div><div className="text-red-400">Bearish</div><div className="text-red-400 font-bold">{bearish}%</div></div>
            <div><div className="text-gray-400">Neutral</div><div className="font-bold">0.0%</div></div>
            <div><div className="text-green-400">Bullish</div><div className="text-green-400 font-bold">{bullish}%</div></div>
          </div>
        </div>

        {/* HIGH PRIORITY NEWS - LIVE */}
        <div className="bg-white rounded-2xl p-4 mb-4 border">
          <div className="flex items-center gap-2 font-bold mb-3"><div className="w-3 h-3 bg-red-500 rounded-full"></div> High Priority News</div>
          {news.map((n,i)=>(
            <div key={i} className="mb-4 border-b pb-3 last:border-0">
              <div className="text-[#0B5FFF] text-sm font-medium leading-tight">{n.title}</div>
              <div className="text-xs text-gray-400 mt-1">{n.date} · {n.pair} · <span className={`px-2 py-0.5 rounded-full text-xs ${n.bias==="Bullish"?"bg-green-100 text-green-700":"bg-red-100 text-red-700"}`}>{n.bias}</span></div>
            </div>
          ))}
        </div>

        {/* FOREX NEWS CARD */}
        <div className="bg-white rounded-2xl p-5 mb-4 border">
          <div className="w-14 h-14 bg-[#0B3D3D] rounded-2xl flex items-center justify-center text-white text-2xl mb-3">📰</div>
          <h3 className="font-bold text-lg">Forex News</h3>
          <p className="text-sm text-gray-500 mt-1">Market mood derived from news analysis and currency impact.</p>
          <button className="mt-4 text-[#0B3D3D] font-bold flex items-center gap-2">View Forex News <span className="w-8 h-8 bg-[#0B3D3D] text-white rounded-full flex items-center justify-center">→</span></button>
        </div>

        {/* INSTITUTIONAL - PREMIUM */}
        <div className="bg-white rounded-2xl p-5 mb-20 border">
          <div className="flex justify-between items-start">
            <div className="w-14 h-14 bg-[#0B3D3D] rounded-2xl flex items-center justify-center text-white text-2xl">↗</div>
            <span className="border px-3 py-1 rounded-full text-xs">Premium</span>
          </div>
          <h3 className="font-bold text-lg mt-3">Institutional Sentiment</h3>
          <p className="text-sm text-gray-500 mt-1">Weekly COT reporting for smart money, commercial, and retail positioning.</p>
          <div className="mt-3 text-xs bg-[#F7F8FA] p-2 rounded">COT Long: <span className="text-blue-600 font-bold">88.95%</span> | Short: 11.05% | Change: <span className="text-red-500">-0.17%</span></div>
          <button className="mt-4 text-[#0B3D3D] font-bold flex items-center gap-2">View COT Reports <span className="w-8 h-8 bg-[#0B3D3D] text-white rounded-full flex items-center justify-center">→</span></button>
        </div>
      </div>
    </div>
  );
}
