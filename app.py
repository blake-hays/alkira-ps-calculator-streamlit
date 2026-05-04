"""
Alkira Professional Services Calculator — Streamlit edition.

Port of dsh4757/PS-Quote-Calculator-SOW- (single-file HTML app) to Streamlit.
Same service catalog, sizing, quote, and SOW output.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass

import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# Branding / page config
# ─────────────────────────────────────────────────────────────────────────────
ALKIRA_BLUE = "#0057B8"
ALKIRA_DARK = "#003A7D"
ALKIRA_ACCENT = "#00A3E0"
ALKIRA_GREEN = "#00B493"
PURPLE = "#7B3FE4"
ORANGE = "#D9500A"
GRAY_400 = "#9AA3B2"
GRAY_600 = "#5A6478"
GRAY_900 = "#1A2333"

st.set_page_config(
    page_title="Alkira Professional Services Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# Catalog: sections + services
# ─────────────────────────────────────────────────────────────────────────────
SECTIONS = [
    {
        "key": "s1",
        "num": "1",
        "title": "Pre-Alkira Implementation Services",
        "subtitle": "Foundation services for successful deployments",
    },
    {
        "key": "s2",
        "num": "2",
        "title": "Backbone-as-a-Service (BaaS)",
        "subtitle": "High-performance cloud-native global backbone services",
    },
    {
        "key": "s3",
        "num": "3",
        "title": "Multi-Cloud Networking (MCN)",
        "subtitle": "Unified connectivity across AWS, Azure, GCP, and on-prem",
    },
    {
        "key": "s4",
        "num": "4",
        "title": "Network & Security Insertion",
        "subtitle": "NGFW, load balancing, DDI, and security service consolidation",
    },
    {
        "key": "s5",
        "num": "5",
        "title": "M&A / B2B Extranet",
        "subtitle": "Rapid, secure onboarding of acquired companies and partners",
    },
]

SECTION_BY_KEY = {s["key"]: s for s in SECTIONS}


@dataclass
class Service:
    id: str
    section: str  # s1..s5
    name: str
    desc: str


SERVICES: list[Service] = [
    Service("1.1", "s1", "Compliance-Driven Network Design",
            "Network and security architectures aligned to regulatory requirements (SOC 2, ISO, PCI, HIPAA)"),
    Service("1.2", "s1", "Network Modernization Assessment",
            "Current-state assessment and phased Alkira-based modernization roadmap"),

    Service("2.1", "s2", "Backbone Architecture & Design",
            "Resilient, high-performance global backbone design aligned to business and connectivity requirements"),
    Service("2.2", "s2", "Backbone Deployment & Configuration",
            "Deploy and configure Alkira backbone across regions for secure, scalable connectivity"),
    Service("2.3", "s2", "Performance Optimization & Validation",
            "Validate and optimize backbone performance for predictable latency, resilience, and application experience"),
    Service("2.4", "s2", "Operational Enablement",
            "Knowledge transfer and training for operations teams to manage and scale the Alkira backbone"),
    Service("2.5", "s2", "Internet-Facing Application Policies",
            "Secure ingress and egress policies for Internet-facing applications using Alkira-integrated services"),
    Service("2.6", "s2", "SD-WAN Integration & Policy",
            "Integrate SD-WAN with Alkira to unify routing, segmentation, and security policies across WAN and cloud"),
    Service("2.7", "s2", "Network Segmentation",
            "Consistent segmentation across the backbone to reduce risk and enforce policy across cloud and on-prem"),
    Service("2.8", "s2", "Compliance-Driven Network Design (BaaS)",
            "Network and security architectures aligned to SOC 2, ISO, PCI, HIPAA within backbone architecture"),
    Service("2.9", "s2", "AWS Direct Connect Configuration",
            "Design and implement AWS Direct Connect integration with Alkira for secure, high-performance private cloud access"),
    Service("2.10", "s2", "Azure ExpressRoute Configuration",
            "Design and integrate Azure ExpressRoute with Alkira to simplify hybrid connectivity and improve performance"),
    Service("2.11", "s2", "Google Interconnect Integration",
            "Integrate Google Cloud Interconnect with Alkira for scalable, low-latency connectivity into GCP environments"),
    Service("2.12", "s2", "IPsec VPN Configuration",
            "Deploy secure IPsec connectivity using Alkira to connect sites, partners, and cloud environments"),
    Service("2.13", "s2", "Global Network Latency Optimization",
            "Optimize global traffic paths to reduce latency and improve application performance across multinational networks"),
    Service("2.14", "s2", "Landing Zone Elimination",
            "Redesign cloud network architecture to eliminate unnecessary landing zones, reducing cost and latency"),

    Service("3.1", "s3", "IPsec VPN Configuration (MCN)",
            "Establish secure connectivity between sites, partners, and multi-cloud environments using Alkira-managed IPsec"),
    Service("3.2", "s3", "Compliance-Driven Network Design (MCN)",
            "Multi-cloud network architectures aligned to regulatory requirements with consistent policy enforcement"),
    Service("3.3", "s3", "AWS Direct Connect Configuration (MCN)",
            "Enable secure, private AWS connectivity within a multi-cloud architecture using Alkira-integrated Direct Connect"),
    Service("3.4", "s3", "Azure ExpressRoute Configuration (MCN)",
            "Integrate Azure ExpressRoute into a unified multi-cloud network using Alkira for simplified connectivity"),
    Service("3.5", "s3", "Google Interconnect Integration (MCN)",
            "Connect Google Cloud into a consistent multi-cloud architecture using Alkira for performance and operational simplicity"),

    Service("4.1", "s4", "Firewall - Insertion & Policy (VNF)",
            "Insert and scale next-generation firewalls without network redesign to centralize security policy"),
    Service("4.2", "s4", "Load Balancer Insertion & Policy (VNF)",
            "Deploy and integrate load balancer VNFs to improve application availability, scalability, and traffic control"),
    Service("4.3", "s4", "DDI Services Insertion & Policy (VNF)",
            "Centralize DNS, DHCP, and IPAM services using policy-driven architecture for improved visibility"),
    Service("4.4", "s4", "SD-WAN Consolidation & Re-Aggregation",
            "Consolidate multiple SD-WAN environments into a unified Alkira-based architecture to reduce cost"),
    Service("4.5", "s4", "Prisma Access Migration",
            "Assess, migrate, and replace Prisma Access with a simplified, cost-optimized Alkira-based architecture"),
    Service("4.6", "s4", "Zscaler Migration",
            "Transition from Zscaler to a modern Alkira-based access architecture to lower costs and improve performance"),

    Service("5.1", "s5", "M&A Network Integration",
            "Rapidly connect and secure parent and acquired networks with minimal disruption using Alkira"),
    Service("5.2", "s5", "Network Segmentation (Extranet)",
            "Consistent network segmentation across cloud and on-prem to reduce attack surface and simplify compliance"),
]

SERVICE_BY_ID = {s.id: s for s in SERVICES}

# Sizing
SIZE_HOURS = {"S": 10, "M": 20, "L": 40, "XL": 60}
SIZE_LABEL = {
    "S": "Small (10 hrs)",
    "M": "Medium (20 hrs)",
    "L": "Large (40 hrs)",
    "XL": "Extra Large (60 hrs)",
    "C": "Custom",
}
SIZE_COLOR = {"S": ALKIRA_GREEN, "M": ALKIRA_BLUE, "L": PURPLE, "XL": ORANGE, "C": GRAY_600}

# Deliverables (used in SOW)
DELIVERABLES: dict[str, list[str]] = {
    "1.1": ["Network and security design aligned to compliance frameworks (SOC 2, ISO, PCI, HIPAA)",
            "Segmentation, logging, and control enforcement",
            "Documentation to support audits"],
    "1.2": ["Current-state architecture and cost analysis",
            "Gap assessment against cloud and security best practices",
            "Future-state Alkira-based modernization roadmap"],
    "2.1": ["Backbone architecture diagram",
            "Traffic flow and resiliency design",
            "Capacity and scalability plan"],
    "2.2": ["Deployed Alkira Backbone as a Service",
            "Configuration documentation",
            "Deployment validation report"],
    "2.3": ["Performance baseline report",
            "Optimization recommendations",
            "Final acceptance sign-off"],
    "2.4": ["Knowledge transfer sessions for operations and network teams",
            "Overview of Alkira portal, monitoring, and change workflows",
            "Best practices documentation for scaling and ongoing optimization"],
    "2.5": ["Ingress and egress policy design",
            "Integration with firewall and load balancer services",
            "Resiliency and security validation report"],
    "2.6": ["SD-WAN integration with Alkira",
            "Centralized routing and security policy definition",
            "Traffic steering and segmentation alignment documentation"],
    "2.7": ["Logical segmentation design across cloud and on-prem",
            "Policy definition and enforcement",
            "Validation and documentation"],
    "2.8": ["Network and security design aligned to compliance frameworks (SOC 2, ISO, PCI, HIPAA) within BaaS architecture",
            "Segmentation, logging, and control enforcement",
            "Documentation to support audits"],
    "2.9": ["AWS Direct Connect design and configuration",
            "High availability and redundancy setup",
            "Routing and traffic validation report"],
    "2.10": ["Azure ExpressRoute design and implementation",
             "Integration with Alkira routing and segmentation",
             "Validation and operational handoff"],
    "2.11": ["Google Interconnect design and onboarding",
             "Integration with Alkira Cloud Area Networking",
             "Routing, policy, and resiliency validation"],
    "2.12": ["IPsec tunnel design and configuration",
             "Encryption and routing policy setup",
             "Redundancy and failover validation"],
    "2.13": ["Global traffic path optimization using Alkira hubs",
             "Regional aggregation and optimized cloud on-ramps",
             "Latency analysis and performance validation report"],
    "2.14": ["Identification of redundant or inefficient landing zones",
             "Network re-design to enable direct, secure application access",
             "Migration and validation planning"],
    "3.1": ["IPsec tunnel design and configuration for multi-cloud environments",
            "Encryption and routing policy setup",
            "Redundancy and failover validation"],
    "3.2": ["Multi-cloud network and security design aligned to compliance frameworks",
            "Segmentation, logging, and control enforcement across environments",
            "Documentation to support audits"],
    "3.3": ["AWS Direct Connect design and configuration within multi-cloud architecture",
            "High availability and redundancy setup",
            "Routing and traffic validation report"],
    "3.4": ["Azure ExpressRoute design and implementation within unified multi-cloud network",
            "Integration with Alkira routing and segmentation",
            "Validation and operational handoff"],
    "3.5": ["Google Interconnect design and onboarding within multi-cloud architecture",
            "Integration with Alkira Cloud Area Networking",
            "Routing, policy, and resiliency validation"],
    "4.1": ["Next-generation firewall insertion without network redesign",
            "Traffic steering and policy enforcement configuration",
            "High availability and scale design"],
    "4.2": ["Load balancer VNF insertion and configuration",
            "L4/L7 policies, health checks, and traffic steering",
            "Integration with segmentation and security services"],
    "4.3": ["Centralized DDI architecture design",
            "Policy-driven DNS, DHCP, and IPAM configuration",
            "Migration and operational handoff"],
    "4.4": ["Assessment of existing SD-WAN vendors and architectures",
            "Consolidation into a unified Alkira-based network fabric",
            "Re-aggregation of regional and global traffic flows"],
    "4.5": ["Current-state assessment of Prisma Access environments",
            "Migration design leveraging Alkira Network Infrastructure-as-a-Service",
            "Cutover execution and decommissioning plan"],
    "4.6": ["Zscaler dependency assessment and exit strategy",
            "Secure access redesign using Alkira-based architectures",
            "Migration, validation, and user cutover"],
    "5.1": ["Rapid connectivity between parent and acquired environments",
            "Temporary and permanent segmentation models",
            "Secure cutover and migration planning"],
    "5.2": ["Logical segmentation design across cloud and on-prem",
            "Policy definition and enforcement",
            "Validation and documentation"],
}


# ─────────────────────────────────────────────────────────────────────────────
# Session-state init
# ─────────────────────────────────────────────────────────────────────────────
def init_state() -> None:
    if "initialized" in st.session_state:
        return
    st.session_state.initialized = True
    st.session_state.hourly_rate = 200
    st.session_state.f_company = ""
    st.session_state.f_contact = ""
    st.session_state.f_title = ""
    st.session_state.f_email = ""
    st.session_state.f_phone = ""
    st.session_state.f_address = ""
    st.session_state.f_quotenum = f"Q-{dt.date.today().year}-001"
    st.session_state.f_preparedby = ""
    st.session_state.f_partnercontact = ""

    # per-service state
    for svc in SERVICES:
        st.session_state[f"sel_{svc.id}"] = False
        st.session_state[f"size_{svc.id}"] = "S"
        st.session_state[f"custom_{svc.id}"] = 10


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────
def hours_for(svc: Service) -> int:
    size = st.session_state.get(f"size_{svc.id}", "S")
    if size == "C":
        return int(st.session_state.get(f"custom_{svc.id}", 10) or 0)
    return SIZE_HOURS.get(size, 10)


def selected_services() -> list[Service]:
    return [s for s in SERVICES if st.session_state.get(f"sel_{s.id}")]


def fmt_money(n: float) -> str:
    return f"${n:,.0f}"


def section_select_all(section_key: str) -> None:
    rows = [s for s in SERVICES if s.section == section_key]
    all_selected = all(st.session_state.get(f"sel_{s.id}") for s in rows)
    new_val = not all_selected
    for s in rows:
        st.session_state[f"sel_{s.id}"] = new_val


def clear_all() -> None:
    for s in SERVICES:
        st.session_state[f"sel_{s.id}"] = False


# ─────────────────────────────────────────────────────────────────────────────
# Styling
# ─────────────────────────────────────────────────────────────────────────────
CSS = f"""
<style>
.app-hero {{
    background: linear-gradient(135deg, {ALKIRA_DARK} 0%, {ALKIRA_BLUE} 100%);
    color: #fff;
    padding: 18px 24px;
    border-radius: 12px;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 16px rgba(0,0,0,.12);
}}
.app-hero h1 {{
    font-size: 22px; margin: 0; font-weight: 700; letter-spacing: .01em;
}}
.app-hero .sub {{
    font-size: 12px; opacity: .82; margin-top: 4px;
}}
.app-hero .logo-mark {{
    width: 44px; height: 44px;
    background: rgba(255,255,255,.18);
    border: 2px solid rgba(255,255,255,.35);
    border-radius: 10px;
    display: inline-flex; align-items: center; justify-content: center;
    font-weight: 900; font-size: 22px;
    margin-right: 14px;
}}
.section-pill {{
    display: inline-block;
    background: {ALKIRA_BLUE};
    color: #fff;
    padding: 2px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .04em;
    margin-right: 8px;
}}
.subtitle {{
    color: {GRAY_600}; font-size: 12px; margin-top: 2px;
}}
.svc-id {{
    display: inline-block;
    background: {ALKIRA_BLUE}; color: #fff;
    padding: 2px 8px; border-radius: 4px;
    font-size: 11px; font-weight: 700; margin-right: 6px;
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
}}
.svc-name {{ font-weight: 600; color: {GRAY_900}; }}
.svc-desc {{ font-size: 12px; color: {GRAY_600}; margin-top: 2px; }}

.metric-card {{
    background: #fff;
    border: 1px solid #EAECF0;
    border-radius: 10px;
    padding: 14px 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,.06);
}}
.metric-card .label {{
    font-size: 11px; font-weight: 700; letter-spacing: .06em;
    color: {GRAY_400}; text-transform: uppercase;
}}
.metric-card .value {{
    font-size: 28px; font-weight: 800; color: {GRAY_900}; margin-top: 4px;
}}
.metric-card .sub {{
    font-size: 12px; color: {GRAY_600}; margin-top: 4px;
}}
.size-badge {{
    display: inline-block;
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
}}

table.ps-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin-top: 8px;
}}
table.ps-table th {{
    text-align: left;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: .06em;
    color: {GRAY_400};
    border-bottom: 2px solid #EAECF0;
    padding: 8px 6px;
}}
table.ps-table td {{
    padding: 10px 6px;
    border-bottom: 1px solid #F2F4F7;
    vertical-align: top;
}}
table.ps-table tr.section-divider td {{
    background: #F7F8FA;
    font-weight: 700;
    color: {GRAY_900};
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: .04em;
    padding: 8px 6px;
}}
table.ps-table td.right {{ text-align: right; font-variant-numeric: tabular-nums; }}
table.ps-table td.center {{ text-align: center; }}

.totals-table {{
    margin-top: 14px;
    width: 320px;
    margin-left: auto;
    border-collapse: collapse;
}}
.totals-table td {{
    padding: 8px 10px;
    font-size: 13px;
    border-bottom: 1px solid #F2F4F7;
}}
.totals-table tr.grand td {{
    font-size: 16px;
    font-weight: 800;
    color: #fff;
    background: {ALKIRA_BLUE};
}}

.sow-section {{
    background: #fff;
    border: 1px solid #EAECF0;
    border-radius: 12px;
    padding: 22px 26px;
    margin-bottom: 16px;
}}
.sow-section h3 {{
    margin: 0 0 12px 0;
    font-size: 16px;
    color: {ALKIRA_DARK};
    border-bottom: 2px solid {ALKIRA_LIGHT_RGBA};
    padding-bottom: 8px;
}}
.sow-prose {{ font-size: 13px; color: {GRAY_900}; line-height: 1.55; }}
.sow-svc {{
    border: 1px solid #EAECF0;
    border-left: 4px solid {ALKIRA_BLUE};
    border-radius: 8px;
    padding: 12px 14px;
    margin-bottom: 10px;
    background: #FCFCFD;
}}
.sow-svc-head {{ display:flex; align-items:center; gap:8px; flex-wrap:wrap; }}
.sow-svc-name {{ font-weight: 700; color: {GRAY_900}; flex: 1; min-width: 220px; }}
.sow-svc-desc {{ font-size: 12px; color: {GRAY_600}; margin-top: 6px; }}
.sow-svc-deliv-title {{
    font-size: 11px; text-transform: uppercase; letter-spacing: .06em;
    color: {GRAY_400}; margin-top: 10px; margin-bottom: 4px; font-weight: 700;
}}
.sow-svc ul {{ margin: 0 0 0 18px; padding: 0; }}
.sow-svc li {{ font-size: 12.5px; color: {GRAY_900}; margin: 2px 0; }}
.sow-cat-label {{
    font-size: 12px; text-transform: uppercase; letter-spacing: .06em;
    color: {GRAY_400}; font-weight: 800; margin: 14px 0 6px;
}}
.sig-grid {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 28px; margin-top: 8px;
}}
.sig-block .role {{
    font-size: 11px; text-transform: uppercase; letter-spacing: .06em;
    color: {GRAY_400}; font-weight: 800; margin-bottom: 14px;
}}
.sig-line {{ border-bottom: 1.5px solid {GRAY_400}; height: 28px; margin-bottom: 4px; }}
.sig-label {{ font-size: 11px; color: {GRAY_600}; }}
</style>
""".replace("{ALKIRA_LIGHT_RGBA}", "rgba(0,87,184,.15)")

st.markdown(CSS, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# App
# ─────────────────────────────────────────────────────────────────────────────
init_state()

st.markdown(
    f"""
    <div class="app-hero">
      <div style="display:flex;align-items:center;">
        <span class="logo-mark">A</span>
        <div>
          <h1>Alkira Professional Services Calculator</h1>
          <div class="sub">Generate Quotes &amp; Statements of Work for Alkira NIaaS engagements</div>
        </div>
      </div>
      <div style="text-align:right;font-size:12px;opacity:.85;">
        {dt.date.today().strftime('%B %d, %Y')}
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar — engagement details
with st.sidebar:
    st.markdown("### Engagement Details")
    st.number_input("Hourly Rate (USD)", min_value=0, step=25, key="hourly_rate")

    st.markdown("---")
    st.markdown("**Customer**")
    st.text_input("Company", key="f_company", placeholder="Acme Corporation")
    st.text_input("Primary Contact", key="f_contact", placeholder="Jane Smith")
    st.text_input("Title", key="f_title", placeholder="VP of Network Engineering")
    st.text_input("Email", key="f_email", placeholder="jane.smith@company.com")
    st.text_input("Phone", key="f_phone", placeholder="+1 (555) 000-0000")
    st.text_input("Address", key="f_address", placeholder="123 Main St, Suite 400, San Jose, CA")

    st.markdown("**Quote / SOW**")
    st.text_input("Quote Number", key="f_quotenum")

    st.markdown("**Prepared By (Partner)**")
    st.text_input("Partner Company", key="f_preparedby", placeholder="Partner Company Name")
    st.text_input("Partner Contact", key="f_partnercontact", placeholder="Partner Rep Name & Email")

    st.markdown("---")
    if st.button("⟳ Reset selections", use_container_width=True):
        clear_all()
        st.rerun()

# Tabs
tab_calc, tab_quote, tab_sow = st.tabs(["🧮 Calculator", "📋 Quote", "📑 SOW"])

# ─────────────────────────────────────────────────────────────────────────────
# CALCULATOR TAB
# ─────────────────────────────────────────────────────────────────────────────
with tab_calc:
    # Top metrics
    sel = selected_services()
    total_hours = sum(hours_for(s) for s in sel)
    rate = float(st.session_state.hourly_rate or 0)
    grand = total_hours * rate

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f"""<div class="metric-card">
                  <div class="label">Services Selected</div>
                  <div class="value">{len(sel)}</div>
                  <div class="sub">of {len(SERVICES)} available</div>
                </div>""",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"""<div class="metric-card">
                  <div class="label">Total Hours</div>
                  <div class="value">{total_hours:,}</div>
                  <div class="sub">at ${rate:,.0f}/hr</div>
                </div>""",
            unsafe_allow_html=True,
        )
    with c3:
        sub = (f"{total_hours:,} total hrs × ${rate:,.0f}/hr"
               if len(sel) > 0 else "Select services below")
        st.markdown(
            f"""<div class="metric-card" style="background:linear-gradient(135deg,{ALKIRA_DARK},{ALKIRA_BLUE});color:#fff;border:none;">
                  <div class="label" style="color:rgba(255,255,255,.75);">Estimated Total</div>
                  <div class="value" style="color:#fff;">{fmt_money(grand)}</div>
                  <div class="sub" style="color:rgba(255,255,255,.75);">{sub}</div>
                </div>""",
            unsafe_allow_html=True,
        )

    st.markdown(" ")

    # Each section as expander
    for section in SECTIONS:
        rows = [s for s in SERVICES if s.section == section["key"]]
        sel_count = sum(1 for s in rows if st.session_state.get(f"sel_{s.id}"))

        with st.expander(
            f"**Section {section['num']}. {section['title']}** — {sel_count} / {len(rows)} selected",
            expanded=(section["key"] == "s1"),
        ):
            st.markdown(
                f"<div class='subtitle'>{section['subtitle']}</div>",
                unsafe_allow_html=True,
            )
            colA, colB = st.columns([6, 1])
            with colB:
                if st.button("Select all", key=f"selall_{section['key']}", use_container_width=True):
                    section_select_all(section["key"])
                    st.rerun()

            for svc in rows:
                with st.container(border=True):
                    top = st.columns([0.07, 0.55, 0.38])
                    with top[0]:
                        st.checkbox(" ", key=f"sel_{svc.id}", label_visibility="collapsed")
                    with top[1]:
                        st.markdown(
                            f"<div><span class='svc-id'>{svc.id}</span>"
                            f"<span class='svc-name'>{svc.name}</span></div>"
                            f"<div class='svc-desc'>{svc.desc}</div>",
                            unsafe_allow_html=True,
                        )
                    with top[2]:
                        st.radio(
                            "Size",
                            options=["S", "M", "L", "XL", "C"],
                            format_func=lambda x: {
                                "S": "S · 10h", "M": "M · 20h", "L": "L · 40h",
                                "XL": "XL · 60h", "C": "Custom",
                            }[x],
                            key=f"size_{svc.id}",
                            horizontal=True,
                            label_visibility="collapsed",
                        )
                        if st.session_state.get(f"size_{svc.id}") == "C":
                            st.number_input(
                                "Custom hours",
                                min_value=1, step=1,
                                key=f"custom_{svc.id}",
                                label_visibility="collapsed",
                            )

# ─────────────────────────────────────────────────────────────────────────────
# QUOTE TAB
# ─────────────────────────────────────────────────────────────────────────────
def render_quote() -> None:
    sel = selected_services()
    rate = float(st.session_state.hourly_rate or 0)
    total_hours = sum(hours_for(s) for s in sel)
    grand = total_hours * rate

    st.markdown(f"## Professional Services Quote")
    meta_l, meta_r = st.columns(2)
    with meta_l:
        st.markdown(
            f"**Quote #:** {st.session_state.f_quotenum or '—'}  \n"
            f"**Date:** {dt.date.today().strftime('%B %d, %Y')}"
        )
    with meta_r:
        st.markdown(
            f"**Prepared For:** {st.session_state.f_company or '—'}  \n"
            f"**Contact:** {st.session_state.f_contact or '—'}"
            + (f" — {st.session_state.f_email}" if st.session_state.f_email else "")
        )

    if st.session_state.f_preparedby:
        st.markdown(
            f"**Prepared By:** {st.session_state.f_preparedby}"
            + (f" ({st.session_state.f_partnercontact})" if st.session_state.f_partnercontact else "")
        )

    st.markdown("---")

    if not sel:
        st.info("No services selected. Switch to the Calculator tab to choose services.")
        return

    # Group by section
    by_section: dict[str, list[Service]] = {sec["key"]: [] for sec in SECTIONS}
    for s in sel:
        by_section[s.section].append(s)

    rows_html = []
    for section in SECTIONS:
        rows = by_section[section["key"]]
        if not rows:
            continue
        rows_html.append(
            f"<tr class='section-divider'><td colspan='5'>{section['num']}. {section['title']}</td></tr>"
        )
        for svc in rows:
            size = st.session_state.get(f"size_{svc.id}", "S")
            hrs = hours_for(svc)
            cost = hrs * rate
            rows_html.append(
                f"<tr>"
                f"<td><span class='svc-id'>{svc.id}</span></td>"
                f"<td><div class='svc-name'>{svc.name}</div>"
                f"<div class='svc-desc'>{svc.desc}</div></td>"
                f"<td class='center'><span class='size-badge' style='background:{SIZE_COLOR[size]}'>{SIZE_LABEL[size]}</span></td>"
                f"<td class='right'>{hrs} hrs</td>"
                f"<td class='right'>{fmt_money(cost)}</td>"
                f"</tr>"
            )

    table_html = (
        "<table class='ps-table'>"
        "<thead><tr>"
        "<th style='width:60px'>ID</th>"
        "<th>Service</th>"
        "<th style='width:130px;text-align:center'>Size</th>"
        "<th style='width:80px;text-align:right'>Hours</th>"
        "<th style='width:120px;text-align:right'>Est. Cost</th>"
        "</tr></thead>"
        "<tbody>" + "".join(rows_html) + "</tbody></table>"
    )
    st.markdown(table_html, unsafe_allow_html=True)

    totals_html = (
        f"<table class='totals-table'>"
        f"<tr><td>Services</td><td class='right'>{len(sel)}</td></tr>"
        f"<tr><td>Total Hours</td><td class='right'>{total_hours:,} hrs</td></tr>"
        f"<tr><td>Hourly Rate</td><td class='right'>{fmt_money(rate)} / hr</td></tr>"
        f"<tr class='grand'><td>Estimated Total</td><td class='right'>{fmt_money(grand)}</td></tr>"
        f"</table>"
    )
    st.markdown(totals_html, unsafe_allow_html=True)

    # Plain-text export
    lines = [
        "ALKIRA PROFESSIONAL SERVICES QUOTE",
        f"Quote #: {st.session_state.f_quotenum or '—'}",
        f"Date: {dt.date.today().strftime('%B %d, %Y')}",
        f"Customer: {st.session_state.f_company or '—'}",
        f"Contact: {st.session_state.f_contact or '—'} ({st.session_state.f_email or ''})",
        "",
        "SELECTED SERVICES",
        "-" * 60,
    ]
    for section in SECTIONS:
        rows = by_section[section["key"]]
        if not rows:
            continue
        lines.append(f"\n{section['num']}. {section['title']}")
        for svc in rows:
            size = st.session_state.get(f"size_{svc.id}", "S")
            hrs = hours_for(svc)
            lines.append(f"  {svc.id}  {svc.name}  [{SIZE_LABEL[size]}]  {hrs} hrs  {fmt_money(hrs*rate)}")
    lines += [
        "",
        f"Total Services: {len(sel)}",
        f"Total Hours:    {total_hours:,}",
        f"Hourly Rate:    {fmt_money(rate)}/hr",
        f"ESTIMATED TOTAL: {fmt_money(grand)}",
    ]
    st.download_button(
        "⬇ Download quote (.txt)",
        data="\n".join(lines),
        file_name=f"{st.session_state.f_quotenum or 'alkira-quote'}.txt",
        mime="text/plain",
    )


with tab_quote:
    render_quote()


# ─────────────────────────────────────────────────────────────────────────────
# SOW TAB
# ─────────────────────────────────────────────────────────────────────────────
def render_sow() -> None:
    sel = selected_services()
    rate = float(st.session_state.hourly_rate or 0)
    total_hours = sum(hours_for(s) for s in sel)
    grand = total_hours * rate
    company = st.session_state.f_company or "the Customer"
    sow_num = (st.session_state.f_quotenum or f"Q-{dt.date.today().year}-001")
    if sow_num.startswith("Q-"):
        sow_num = "SOW-" + sow_num[2:]
    elif not sow_num.startswith("SOW-"):
        sow_num = "SOW-" + sow_num

    st.markdown(f"## Statement of Work — {sow_num}")
    st.markdown(f"**Date:** {dt.date.today().strftime('%B %d, %Y')}")

    # Header table
    header_md = (
        "| | |\n|---|---|\n"
        f"| **Customer** | {st.session_state.f_company or '—'} |\n"
        f"| **Contact** | {st.session_state.f_contact or '—'} |\n"
        f"| **Title** | {st.session_state.f_title or '—'} |\n"
        f"| **Email** | {st.session_state.f_email or '—'} |\n"
        f"| **Phone** | {st.session_state.f_phone or '—'} |\n"
        f"| **Address** | {st.session_state.f_address or '—'} |\n"
        f"| **Prepared By** | {st.session_state.f_preparedby or '—'} |\n"
        f"| **Partner Contact** | {st.session_state.f_partnercontact or '—'} |\n"
    )
    st.markdown(header_md)
    st.markdown("---")

    # Section 1
    s1 = (
        f"<div class='sow-section'>"
        f"<h3>1. Executive Summary</h3>"
        f"<p class='sow-prose'>This Statement of Work (SOW) defines the professional services to be delivered "
        f"by the Service Provider to <strong>{company}</strong> in connection with the implementation of "
        f"Alkira's Network Infrastructure as a Service (NIaaS) platform. The objective of this engagement is "
        f"to accelerate time-to-value, reduce deployment risk, and modernize the customer's network and "
        f"security architecture across cloud and on-premises environments.</p>"
        f"<p class='sow-prose' style='margin-top:10px;'>This SOW encompasses {len(sel)} professional "
        f"service{'s' if len(sel) != 1 else ''} totaling <strong>{total_hours:,} hours</strong> at an "
        f"estimated total investment of <strong>{fmt_money(grand)}</strong>.</p>"
        f"</div>"
    )
    st.markdown(s1, unsafe_allow_html=True)

    # Section 2 — scope
    parts = ["<div class='sow-section'><h3>2. Scope of Work</h3>"]
    if not sel:
        parts.append("<p class='sow-prose'><em>No services selected — go back to the Calculator tab.</em></p>")
    else:
        by_section: dict[str, list[Service]] = {sec["key"]: [] for sec in SECTIONS}
        for s in sel:
            by_section[s.section].append(s)
        for section in SECTIONS:
            rows = by_section[section["key"]]
            if not rows:
                continue
            parts.append(f"<div class='sow-cat-label'>{section['num']}. {section['title']}</div>")
            for svc in rows:
                size = st.session_state.get(f"size_{svc.id}", "S")
                hrs = hours_for(svc)
                delivs = DELIVERABLES.get(svc.id, ["Deliverables to be defined during project kickoff"])
                deliv_html = "".join(f"<li>{d}</li>" for d in delivs)
                parts.append(
                    f"<div class='sow-svc'>"
                    f"<div class='sow-svc-head'>"
                    f"<span class='svc-id'>{svc.id}</span>"
                    f"<span class='sow-svc-name'>{svc.name}</span>"
                    f"<span class='size-badge' style='background:{SIZE_COLOR[size]}'>{SIZE_LABEL[size]}</span>"
                    f"<span class='size-badge' style='background:{GRAY_600}'>{hrs} hrs</span>"
                    f"</div>"
                    f"<div class='sow-svc-desc'>{svc.desc}</div>"
                    f"<div class='sow-svc-deliv-title'>Deliverables</div>"
                    f"<ul>{deliv_html}</ul>"
                    f"</div>"
                )
    parts.append("</div>")
    st.markdown("".join(parts), unsafe_allow_html=True)

    # Section 3 — terms
    terms_html = (
        f"<div class='sow-section'><h3>3. Engagement Terms</h3>"
        f"<table class='ps-table' style='width:100%;'>"
        f"<tr><td>Engagement Type</td><td>Time &amp; Materials</td></tr>"
        f"<tr><td>Total Services</td><td>{len(sel)} service{'s' if len(sel) != 1 else ''}</td></tr>"
        f"<tr><td>Total Estimated Hours</td><td>{total_hours:,} hours</td></tr>"
        f"<tr><td>Hourly Rate</td><td>{fmt_money(rate)} / hour</td></tr>"
        f"<tr><td>Payment Terms</td><td>Net 30 from invoice date</td></tr>"
        f"<tr><td>Quote / SOW Reference</td><td>{st.session_state.f_quotenum or '—'}</td></tr>"
        f"<tr style='background:{ALKIRA_BLUE};color:#fff;font-weight:800;'>"
        f"<td style='color:#fff;'>Total Estimated Investment</td>"
        f"<td style='color:#fff;'>{fmt_money(grand)}</td></tr>"
        f"</table></div>"
    )
    st.markdown(terms_html, unsafe_allow_html=True)

    # Section 4 — assumptions
    assumptions = [
        "Customer will provide timely access to relevant network documentation, architecture diagrams, and key stakeholders.",
        "Customer will designate a primary point of contact and a project sponsor for the duration of the engagement.",
        "Customer has or will procure the necessary Alkira platform licenses prior to the start of implementation services.",
        "Cloud provider accounts (AWS, Azure, GCP) will be provisioned and accessible by the project start date.",
        "Any out-of-scope work identified during the engagement will be addressed via a written Change Order prior to execution.",
        "Travel expenses, if required, will be billed separately at cost and require prior written approval.",
        "Estimated hours are based on standard complexity. Significant deviations in scope may require a revised SOW.",
    ]
    a_html = "".join(f"<li>{a}</li>" for a in assumptions)
    st.markdown(
        f"<div class='sow-section'><h3>4. Assumptions &amp; Dependencies</h3>"
        f"<ul class='sow-prose'>{a_html}</ul></div>",
        unsafe_allow_html=True,
    )

    # Section 5 — signatures
    sig_html = (
        "<div class='sow-section'><h3>5. Acceptance &amp; Signatures</h3>"
        "<p class='sow-prose'>By signing below, both parties agree to the terms and scope defined in this "
        "Statement of Work. This SOW is subject to the Master Services Agreement or equivalent agreement "
        "between the parties.</p>"
        "<div class='sig-grid'>"
        "<div class='sig-block'>"
        "<div class='role'>Customer Authorization</div>"
        "<div class='sig-line'></div><div class='sig-label'>Signature</div>"
        "<div class='sig-line' style='margin-top:18px'></div><div class='sig-label'>Printed Name &amp; Title</div>"
        "<div class='sig-line' style='margin-top:18px'></div><div class='sig-label'>Date</div>"
        "</div>"
        "<div class='sig-block'>"
        "<div class='role'>Service Provider Authorization</div>"
        "<div class='sig-line'></div><div class='sig-label'>Signature</div>"
        "<div class='sig-line' style='margin-top:18px'></div><div class='sig-label'>Printed Name &amp; Title</div>"
        "<div class='sig-line' style='margin-top:18px'></div><div class='sig-label'>Date</div>"
        "</div>"
        "</div></div>"
    )
    st.markdown(sig_html, unsafe_allow_html=True)

    # Markdown export
    md_lines = [
        f"# Statement of Work — {sow_num}",
        f"_Date: {dt.date.today().strftime('%B %d, %Y')}_",
        "",
        f"**Customer:** {st.session_state.f_company or '—'}  ",
        f"**Contact:** {st.session_state.f_contact or '—'}  ",
        f"**Email:** {st.session_state.f_email or '—'}  ",
        f"**Prepared By:** {st.session_state.f_preparedby or '—'}",
        "",
        "## 1. Executive Summary",
        f"This SOW defines professional services to be delivered to **{company}** in connection with the "
        f"implementation of Alkira's NIaaS platform. It encompasses {len(sel)} service"
        f"{'s' if len(sel) != 1 else ''} totaling **{total_hours:,} hours** at an estimated investment of "
        f"**{fmt_money(grand)}**.",
        "",
        "## 2. Scope of Work",
    ]
    if sel:
        by_section = {sec["key"]: [] for sec in SECTIONS}
        for s in sel:
            by_section[s.section].append(s)
        for section in SECTIONS:
            rows = by_section[section["key"]]
            if not rows:
                continue
            md_lines.append(f"\n### {section['num']}. {section['title']}\n")
            for svc in rows:
                size = st.session_state.get(f"size_{svc.id}", "S")
                hrs = hours_for(svc)
                md_lines.append(
                    f"**{svc.id} — {svc.name}** _({SIZE_LABEL[size]}, {hrs} hrs)_  \n{svc.desc}\n"
                )
                md_lines.append("Deliverables:")
                for d in DELIVERABLES.get(svc.id, ["TBD during kickoff"]):
                    md_lines.append(f"- {d}")
                md_lines.append("")
    else:
        md_lines.append("_No services selected._")

    md_lines += [
        "",
        "## 3. Engagement Terms",
        "| Item | Value |",
        "|---|---|",
        "| Engagement Type | Time & Materials |",
        f"| Total Services | {len(sel)} |",
        f"| Total Estimated Hours | {total_hours:,} |",
        f"| Hourly Rate | {fmt_money(rate)} / hr |",
        "| Payment Terms | Net 30 |",
        f"| **Total Estimated Investment** | **{fmt_money(grand)}** |",
        "",
        "## 4. Assumptions & Dependencies",
        *(f"- {a}" for a in assumptions),
        "",
        "## 5. Acceptance & Signatures",
        "*Customer Authorization* — Signature / Printed Name & Title / Date",
        "",
        "*Service Provider Authorization* — Signature / Printed Name & Title / Date",
    ]
    st.download_button(
        "⬇ Download SOW (.md)",
        data="\n".join(md_lines),
        file_name=f"{sow_num}.md",
        mime="text/markdown",
    )


with tab_sow:
    render_sow()
