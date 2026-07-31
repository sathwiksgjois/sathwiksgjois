<div align="center">

<img src="assets/hero-banner.svg" alt="Sathwik S G Jois — AI Systems · Backend · Distributed Systems Engineer" width="100%"/>

<br/>

<a href="https://github.com/sathwiksgjois">
  <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=20&duration=2600&pause=1200&color=A78BFA&center=true&vCenter=true&width=680&lines=Designing+distributed+systems+that+don't+fall+over;Building+retrieval+and+reasoning+pipelines+for+LEXOS;Writing+a+Redis+clone+in+modern+C%2B%2B+from+epoll+up;Shipping+multi-agent+AI+platforms%2C+not+demos" alt="Typing SVG" />
</a>

<br/><br/>

<a href="mailto:sathwiksg31@gmail.com"><img src="https://img.shields.io/badge/-Email-0B0E1A?style=flat-square&logo=gmail&logoColor=E5E7EB&labelColor=0B0E1A" /></a>
<a href="https://www.linkedin.com/in/sathwik-s-g-129880310/"><img src="https://img.shields.io/badge/-LinkedIn-0B0E1A?style=flat-square&logo=linkedin&logoColor=E5E7EB&labelColor=0B0E1A" /></a>
<a href="https://github.com/sathwiksgjois"><img src="https://img.shields.io/badge/-GitHub-0B0E1A?style=flat-square&logo=github&logoColor=E5E7EB&labelColor=0B0E1A" /></a>
<a href="#"><img src="https://img.shields.io/badge/-Resume-0B0E1A?style=flat-square&logo=readdotcv&logoColor=E5E7EB&labelColor=0B0E1A" /></a>
<img src="https://komarev.com/ghpvc/?username=sathwiksgjois&style=flat-square&color=6366f1&label=Profile+Views" />

</div>

<img src="assets/divider.svg" width="100%" />

## <img src="assets/section-tag.svg" height="8"/>&nbsp; About

I work on the parts of software that are hard to get right the first time: retrieval pipelines that need to be *correct*, event loops that need to not drop connections, and agent systems that need to know when to stop talking. Based in India, currently focused on production-grade AI systems, distributed infrastructure, and the backend architecture underneath both.

**Interested in**

<table>
<tr>
<td width="20%" align="center">AI Systems</td>
<td width="20%" align="center">Agentic AI</td>
<td width="20%" align="center">Distributed Systems</td>
<td width="20%" align="center">Backend Engineering</td>
<td width="20%" align="center">Networking</td>
</tr>
<tr>
<td width="20%" align="center">Operating Systems</td>
<td width="20%" align="center">Retrieval-Augmented Generation</td>
<td width="20%" align="center">System Design</td>
<td width="20%" align="center">Databases</td>
<td width="20%" align="center">Developer Infrastructure</td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" />

## <img src="assets/section-tag.svg" height="8"/>&nbsp; Engineering Dashboard

<table>
<tr><td><b>Current Focus</b></td><td>Production-grade retrieval and multi-agent reasoning for <a href="#-lexos">LEXOS</a></td></tr>
<tr><td><b>Currently Learning</b></td><td>Consensus protocols, storage-engine internals, and large-scale agent orchestration</td></tr>
<tr><td><b>Building</b></td><td>A C++ in-memory data store from raw sockets up — <a href="#-novacache">NovaCache</a></td></tr>
<tr><td><b>Open to Collaborate On</b></td><td>AI infrastructure, RAG systems, and low-level networking/storage projects</td></tr>
<tr><td><b>Latest Interests</b></td><td>Cross-encoder reranking, knowledge graphs for legal reasoning, event-driven architectures</td></tr>
</table>

<img src="assets/divider.svg" width="100%" />

## <img src="assets/section-tag.svg" height="8"/>&nbsp; Featured Projects

### <a name="-lexos"></a>LEXOS — AI Litigation Intelligence Platform
<sub>FLAGSHIP PROJECT &nbsp;·&nbsp; ENTERPRISE-SCALE AI PLATFORM</sub>

An end-to-end AI system for legal reasoning: it retrieves authorities, verifies citations against source text, and runs a structured multi-agent debate before producing a drafted memorial — rather than a single-shot LLM answer.

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor':'#161233','primaryTextColor':'#E5E7EB','primaryBorderColor':'#6366F1','lineColor':'#8B5CF6','secondaryColor':'#0f172a','tertiaryColor':'#0b0e1a','fontFamily':'Fira Code'}}}%%
flowchart LR
    Q[Query] --> QU[Query Understanding]
    QU --> SR[Semantic Retrieval<br/>Vector Index]
    QU --> KG[Knowledge Graph<br/>Traversal]
    SR --> AP[Authority Pool<br/>Construction]
    KG --> AP
    AP --> RR[Cross-Encoder<br/>Reranking]
    RR --> DE{Multi-Agent<br/>Debate Engine}
    DE --> PA[Prosecuting Agent]
    DE --> DA[Defending Agent]
    PA --> JA[Judge Agent]
    DA --> JA
    JA --> CV[Citation<br/>Verification]
    CV --> MG[Memorial<br/>Generation]
    MG --> OUT[Drafted Output]
```

<details>
<summary><b>Tech stack &amp; key innovations</b></summary>
<br/>

| | |
|---|---|
| **Retrieval** | Semantic vector search, hybrid dense + sparse retrieval, legal corpus indexing |
| **Reasoning** | Multi-agent debate engine with role-conditioned agents and a judge agent for adjudication |
| **Grounding** | Citation verification layer that checks generated claims against indexed source text |
| **Knowledge** | Domain knowledge graph for statute/precedent relationships, traversed alongside vector retrieval |
| **Reranking** | Cross-encoder reranking over the authority pool before it reaches the debate engine |
| **Output** | Structured memorial generation from verified, reranked evidence |

**Key innovations**
- Two-stage retrieval (semantic + graph) merged into a single authority pool before reranking, instead of relying on vector search alone
- A debate-structured reasoning loop, so conclusions come from adjudicated argument rather than a single forward pass
- Citation verification as a hard gate — claims that can't be traced to source text don't reach the final draft

</details>

<br/>

### <a name="-astrafund"></a>AstraFund — Multi-Agent Trading Platform
<sub>AGENT ORCHESTRATION &nbsp;·&nbsp; LANGGRAPH</sub>

A trading research platform where specialized agents own specialized concerns — market state, news sentiment, risk, strategy — and a judge agent resolves their (often conflicting) outputs into a single execution decision.

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor':'#161233','primaryTextColor':'#E5E7EB','primaryBorderColor':'#6366F1','lineColor':'#8B5CF6','secondaryColor':'#0f172a','tertiaryColor':'#0b0e1a','fontFamily':'Fira Code'}}}%%
flowchart TD
    YF[Yahoo Finance<br/>Market Data] --> MA[Market Agent]
    NW[News Sources] --> NA[News Agent]
    MA --> SG[Signal Generation]
    NA --> SG
    SG --> RA[Risk Agent]
    SG --> STA[Strategy Agent]
    RA --> JA[Judge Agent<br/>LangGraph Orchestrator]
    STA --> JA
    JA --> EA[Execution Agent]
    EA --> BT[Backtesting Engine]
    EA --> PF[Portfolio Analytics]
```

<details>
<summary><b>Tech stack &amp; key innovations</b></summary>
<br/>

| | |
|---|---|
| **Orchestration** | LangGraph-based agent graph with explicit state transitions between agents |
| **Agents** | Market, News, Risk, Strategy, Judge, and Execution agents, each with a narrow, testable responsibility |
| **Data** | Yahoo Finance market data feed |
| **Evaluation** | Backtesting engine and portfolio analytics for measuring strategy performance over historical data |

**Key innovations**
- Risk and Strategy agents run independently and are only reconciled by a dedicated Judge agent — no single agent has unchecked authority over execution
- Signal generation is decoupled from decision-making, so new data sources can plug into the same agent graph

</details>

<br/>

### <a name="-novacache"></a>NovaCache — A Redis Clone in Modern C++
<sub>SYSTEMS PROGRAMMING &nbsp;·&nbsp; C++ &nbsp;·&nbsp; EPOLL</sub>

An in-memory key-value store built from the socket layer up: a non-blocking TCP server on an `epoll` event loop, a hand-written RESP parser, and a storage engine with TTL and persistence — no framework in between.

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor':'#161233','primaryTextColor':'#E5E7EB','primaryBorderColor':'#6366F1','lineColor':'#8B5CF6','secondaryColor':'#0f172a','tertiaryColor':'#0b0e1a','fontFamily':'Fira Code'}}}%%
flowchart LR
    C[Client] --> TCP[Non-blocking<br/>TCP Server]
    TCP --> EL[epoll<br/>Event Loop]
    EL --> RP[RESP Parser]
    RP --> CD[Command Dispatcher]
    CD --> SE[Storage Engine]
    SE --> TTL[TTL Wheel]
    SE --> PS[Persistence<br/>Snapshot / Log]
    CD --> RE[Response Encoder]
    RE --> C
```

<details>
<summary><b>Tech stack &amp; key innovations</b></summary>
<br/>

| | |
|---|---|
| **Networking** | Custom non-blocking TCP server, `epoll`-based event loop, no external networking library |
| **Protocol** | Hand-written RESP parser compatible with standard Redis clients |
| **Storage** | In-memory storage engine with TTL expiry and thread-safe access |
| **Durability** | Persistence layer for surviving restarts |
| **Concurrency** | Thread-safety across the storage layer under concurrent connections |

**Key innovations**
- Single-threaded event loop for the network layer keeps the RESP protocol handling free of lock contention, while the storage layer is still safe under concurrent access
- TTL expiry implemented without scanning the whole keyspace on every tick

</details>

<br/>

<table>
<tr>
<td width="50%" valign="top">

### AuraChat — Secure AI Chat Platform
<sub>REAL-TIME &nbsp;·&nbsp; ENCRYPTED</sub>

A messaging platform with JWT-based authentication and end-to-end AES encryption, layered with AI-native features: summarization, translation, and sentiment analysis on top of real-time WebSocket messaging.

**Tech stack**
`JWT` `AES-256` `WebSockets` `Real-time messaging` `AI summarization` `Translation` `Sentiment analysis`

</td>
<td width="50%" valign="top">

### CommerceHub — Multi-Vendor Commerce Backend
<sub>BACKEND &nbsp;·&nbsp; MARKETPLACE</sub>

A backend for a multi-vendor e-commerce marketplace — vendor accounts, catalog and inventory management, and order flows modeled as independent, composable services rather than a single monolithic store.

**Tech stack**
`REST APIs` `Multi-vendor architecture` `Order management` `Inventory` `Auth`

</td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" />

## <img src="assets/section-tag.svg" height="8"/>&nbsp; Skills

<table>
<tr>
<td valign="top" width="50%">

**AI Systems**

<img src="https://img.shields.io/badge/-LangChain-6366F1?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/-LangGraph-6366F1?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/-RAG-6366F1?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/-Prompt%20Engineering-6366F1?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/-Vector%20Search-6366F1?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/-Embeddings-6366F1?style=flat-square&logoColor=white" />

**Backend**

<img src="https://img.shields.io/badge/-Django-8B5CF6?style=flat-square&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/-Spring%20Boot-8B5CF6?style=flat-square&logo=springboot&logoColor=white" />
<img src="https://img.shields.io/badge/-FastAPI-8B5CF6?style=flat-square&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/-REST-8B5CF6?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/-JWT-8B5CF6?style=flat-square&logo=jsonwebtokens&logoColor=white" />

</td>
<td valign="top" width="50%">

**Distributed Systems**

<img src="https://img.shields.io/badge/-Redis-22D3EE?style=flat-square&logo=redis&logoColor=white" />
<img src="https://img.shields.io/badge/-epoll-22D3EE?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/-Sockets-22D3EE?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/-TCP%2FIP-22D3EE?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/-Concurrency-22D3EE?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/-Storage%20Engines-22D3EE?style=flat-square&logoColor=white" />

**Databases**

<img src="https://img.shields.io/badge/-PostgreSQL-A78BFA?style=flat-square&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/-Redis-A78BFA?style=flat-square&logo=redis&logoColor=white" />
<img src="https://img.shields.io/badge/-SQLite-A78BFA?style=flat-square&logo=sqlite&logoColor=white" />

</td>
</tr>
</table>

<details>
<summary><b>Full development toolchain</b></summary>
<br/>

<img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/-C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" />
<img src="https://img.shields.io/badge/-Java-007396?style=flat-square&logo=openjdk&logoColor=white" />
<img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black" />
<img src="https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/-CMake-064F8C?style=flat-square&logo=cmake&logoColor=white" />

</details>

<img src="assets/divider.svg" width="100%" />

## <img src="assets/section-tag.svg" height="8"/>&nbsp; Roadmap

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor':'#161233','primaryTextColor':'#E5E7EB','primaryBorderColor':'#6366F1','lineColor':'#8B5CF6','cScale0':'#161233','cScale1':'#1e1b3a','cScale2':'#0f172a','fontFamily':'Fira Code'}}}%%
timeline
    title Engineering Journey
    2024 : Backend Foundations
         : Django
         : Spring Boot
         : System Design
    2025 : Distributed Systems & AI
         : NovaCache
         : Networking
         : Agentic AI
         : RAG
         : LEXOS
         : AstraFund
    2026 : Production & Infra
         : Production AI Platforms
         : Infrastructure
         : Open Source
```

<img src="assets/divider.svg" width="100%" />

## <img src="assets/section-tag.svg" height="8"/>&nbsp; GitHub Metrics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=sathwiksgjois&show_icons=true&hide_border=true&bg_color=00000000&title_color=A78BFA&icon_color=22D3EE&text_color=9CA3AF&count_private=true" width="49%" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=sathwiksgjois&layout=compact&hide_border=true&bg_color=00000000&title_color=A78BFA&text_color=9CA3AF&langs_count=8" width="30%" />

<br/>

<img src="https://streak-stats.demolab.com?user=sathwiksgjois&hide_border=true&background=00000000&ring=6366F1&fire=22D3EE&currStreakLabel=A78BFA&sideLabels=9CA3AF&currStreakNum=E5E7EB&sideNums=E5E7EB&dates=6B7280" width="49%" />

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=sathwiksgjois&theme=react-dark&hide_border=true&bg_color=00000000&color=9CA3AF&line=6366F1&point=22D3EE" width="80%" />

</div>

<details>
<summary><b>Trophy case</b></summary>
<br/>
<div align="center">
<img src="https://github-profile-trophy.vercel.app/?username=sathwiksgjois&theme=algolia&no-frame=true&no-bg=true&row=1&column=7" />
</div>
</details>

<img src="assets/divider.svg" width="100%" />

## <img src="assets/section-tag.svg" height="8"/>&nbsp; Contribution Graph

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sathwiksgjois/sathwiksgjois/output/dist/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sathwiksgjois/sathwiksgjois/output/dist/snake-light.svg" />
  <img alt="contribution snake animation" src="https://raw.githubusercontent.com/sathwiksgjois/sathwiksgjois/output/dist/snake-dark.svg" width="100%" />
</picture>
</div>

<img src="assets/divider.svg" width="100%" />

## <img src="assets/section-tag.svg" height="8"/>&nbsp; Latest Activity

<!--START_ACTIVITY-->
- Recent public activity refreshes automatically here via `.github/workflows/update-readme.yml`
<!--END_ACTIVITY-->

<img src="assets/footer.svg" width="100%" />

