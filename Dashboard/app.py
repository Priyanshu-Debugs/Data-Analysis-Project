"""
Dynamic Power BI-Style Dashboard for Data Analysis Projects
Includes: Bank Loan Analysis & Blinkit Sales Analysis
"""

import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
import os

# Initialize the Dash app with a modern theme
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY, dbc.icons.FONT_AWESOME],
    suppress_callback_exceptions=True,
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}]
)

app.title = "Data Analysis Dashboard"

# Custom CSS for dropdown styling
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            /* Dropdown container styling */
            .Select-control {
                background-color: #1a1a2e !important;
                border-color: #0f3460 !important;
            }
            
            /* Dropdown menu styling */
            .Select-menu-outer {
                background-color: #16213e !important;
                border: 1px solid #0f3460 !important;
            }
            
            /* Dropdown options styling */
            .VirtualizedSelectOption {
                background-color: #16213e !important;
                color: #ffffff !important;
            }
            
            .VirtualizedSelectFocusedOption {
                background-color: #3498db !important;
                color: #ffffff !important;
            }
            
            /* Modern Dash dropdown styling */
            .dash-dropdown .Select-control {
                background-color: #1a1a2e !important;
                border-color: #0f3460 !important;
                color: #ffffff !important;
            }
            
            .dash-dropdown .Select-menu-outer {
                background-color: #16213e !important;
                border: 1px solid #0f3460 !important;
                z-index: 9999 !important;
            }
            
            .dash-dropdown .Select-option {
                background-color: #16213e !important;
                color: #ffffff !important;
                padding: 10px 12px !important;
            }
            
            .dash-dropdown .Select-option:hover,
            .dash-dropdown .Select-option.is-focused {
                background-color: #3498db !important;
                color: #ffffff !important;
            }
            
            .dash-dropdown .Select-option.is-selected {
                background-color: #2ecc71 !important;
                color: #ffffff !important;
            }
            
            .dash-dropdown .Select-value-label,
            .dash-dropdown .Select-placeholder {
                color: #dfe6e9 !important;
            }
            
            .dash-dropdown .Select-input input {
                color: #ffffff !important;
            }
            
            .dash-dropdown .Select-arrow {
                border-color: #dfe6e9 transparent transparent !important;
            }
            
            .dash-dropdown .Select.is-open .Select-arrow {
                border-color: transparent transparent #dfe6e9 !important;
            }
            
            /* Clear button styling */
            .dash-dropdown .Select-clear {
                color: #dfe6e9 !important;
            }
            
            .dash-dropdown .Select-clear:hover {
                color: #e74c3c !important;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# ======================== DATA LOADING ========================

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)

def load_bank_loan_data():
    """Load and preprocess bank loan data"""
    try:
        file_path = os.path.join(BASE_DIR, "Bank-Loan-Analysis", "financial_loan.xlsx")
        df = pd.read_excel(file_path)
        df['issue_date'] = pd.to_datetime(df['issue_date'])
        df['month_name'] = df['issue_date'].dt.strftime('%b %Y')
        df['month_num'] = df['issue_date'].dt.to_period('M')
        return df
    except Exception as e:
        print(f"Error loading bank loan data: {e}")
        return None

def load_blinkit_data():
    """Load and preprocess Blinkit data"""
    try:
        file_path = os.path.join(BASE_DIR, "Blinkit-Sales-Analysis", "blinkit_data.csv")
        df = pd.read_csv(file_path)
        # Clean Item Fat Content
        df['Item Fat Content'] = df['Item Fat Content'].replace({
            'LF': 'Low Fat',
            'low fat': 'Low Fat',
            'reg': 'Regular'
        })
        return df
    except Exception as e:
        print(f"Error loading Blinkit data: {e}")
        return None

# Load data
bank_df = load_bank_loan_data()
blinkit_df = load_blinkit_data()

# ======================== STYLING ========================

COLORS = {
    'primary': '#3498db',
    'success': '#2ecc71',
    'warning': '#f39c12',
    'danger': '#e74c3c',
    'info': '#00cec9',
    'dark': '#2d3436',
    'light': '#dfe6e9',
    'background': '#1a1a2e',
    'card': '#16213e',
    'card_border': '#0f3460'
}

CARD_STYLE = {
    'backgroundColor': COLORS['card'],
    'borderRadius': '15px',
    'padding': '20px',
    'marginBottom': '20px',
    'border': f'1px solid {COLORS["card_border"]}',
    'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.3)'
}

KPI_CARD_STYLE = {
    'backgroundColor': COLORS['card'],
    'borderRadius': '15px',
    'padding': '25px',
    'textAlign': 'center',
    'border': f'1px solid {COLORS["card_border"]}',
    'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.3)',
    'minHeight': '150px'
}

# ======================== HELPER FUNCTIONS ========================

def create_kpi_card(title, value, icon, color, delta=None, delta_text=None):
    """Create a KPI card component"""
    delta_component = []
    if delta is not None:
        delta_color = COLORS['success'] if delta >= 0 else COLORS['danger']
        delta_icon = "fa-arrow-up" if delta >= 0 else "fa-arrow-down"
        delta_component = html.Div([
            html.I(className=f"fas {delta_icon}", style={'color': delta_color, 'marginRight': '5px'}),
            html.Span(f"{abs(delta):.1f}%", style={'color': delta_color, 'fontSize': '14px'}),
            html.Span(f" {delta_text}" if delta_text else "", style={'color': COLORS['light'], 'fontSize': '12px'})
        ], style={'marginTop': '10px'})
    
    return dbc.Card([
        dbc.CardBody([
            html.Div([
                html.I(className=f"fas {icon}", style={'fontSize': '30px', 'color': color}),
            ], style={'marginBottom': '15px'}),
            html.H6(title, style={'color': COLORS['light'], 'marginBottom': '10px', 'fontSize': '14px'}),
            html.H3(value, style={'color': 'white', 'fontWeight': 'bold', 'marginBottom': '0'}),
            delta_component
        ])
    ], style=KPI_CARD_STYLE)

# ======================== NAVIGATION ========================

navbar = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col(html.I(className="fas fa-chart-line", style={'fontSize': '24px', 'color': COLORS['primary']})),
            dbc.Col(dbc.NavbarBrand("Analytics Dashboard", className="ms-2", style={'fontWeight': 'bold', 'fontSize': '20px'})),
        ], align="center", className="g-0"),
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Bank Loan", href="/bank-loan", id="nav-bank", active=True)),
            dbc.NavItem(dbc.NavLink("Blinkit Sales", href="/blinkit", id="nav-blinkit")),
        ], className="ms-auto", navbar=True)
    ], fluid=True),
    color="dark",
    dark=True,
    sticky="top",
    style={'marginBottom': '20px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.3)'}
)

# ======================== BANK LOAN DASHBOARD ========================

def create_bank_loan_dashboard():
    """Create Bank Loan Analysis Dashboard"""
    if bank_df is None:
        return html.Div("Error loading Bank Loan data", style={'color': 'red', 'textAlign': 'center', 'padding': '50px'})
    
    # Calculate KPIs
    total_applications = len(bank_df)
    total_funded = bank_df['loan_amount'].sum()
    total_received = bank_df['total_payment'].sum()
    avg_interest_rate = bank_df['int_rate'].mean() * 100
    avg_dti = bank_df['dti'].mean() * 100
    
    # Good/Bad Loan Metrics
    good_loans = bank_df[bank_df['loan_status'].isin(['Fully Paid', 'Current'])]
    bad_loans = bank_df[bank_df['loan_status'] == 'Charged Off']
    good_loan_pct = (len(good_loans) / total_applications) * 100
    bad_loan_pct = (len(bad_loans) / total_applications) * 100
    
    # MTD Calculations
    latest_date = bank_df['issue_date'].max()
    mtd_data = bank_df[(bank_df['issue_date'].dt.year == latest_date.year) & 
                       (bank_df['issue_date'].dt.month == latest_date.month)]
    mtd_applications = len(mtd_data)
    mtd_funded = mtd_data['loan_amount'].sum()
    
    return html.Div([
        # Filters Row
        dbc.Row([
            dbc.Col([
                html.Label("Select State", style={'color': COLORS['light'], 'marginBottom': '5px'}),
                dcc.Dropdown(
                    id='bank-state-filter',
                    options=[{'label': 'All States', 'value': 'all'}] + 
                            [{'label': s, 'value': s} for s in sorted(bank_df['address_state'].unique())],
                    value='all',
                    style={'backgroundColor': COLORS['card']}
                )
            ], md=3),
            dbc.Col([
                html.Label("Loan Purpose", style={'color': COLORS['light'], 'marginBottom': '5px'}),
                dcc.Dropdown(
                    id='bank-purpose-filter',
                    options=[{'label': 'All Purposes', 'value': 'all'}] + 
                            [{'label': p.title(), 'value': p} for p in sorted(bank_df['purpose'].unique())],
                    value='all',
                    style={'backgroundColor': COLORS['card']}
                )
            ], md=3),
            dbc.Col([
                html.Label("Loan Term", style={'color': COLORS['light'], 'marginBottom': '5px'}),
                dcc.Dropdown(
                    id='bank-term-filter',
                    options=[{'label': 'All Terms', 'value': 'all'}] + 
                            [{'label': t, 'value': t} for t in sorted(bank_df['term'].unique())],
                    value='all',
                    style={'backgroundColor': COLORS['card']}
                )
            ], md=3),
            dbc.Col([
                html.Label("Home Ownership", style={'color': COLORS['light'], 'marginBottom': '5px'}),
                dcc.Dropdown(
                    id='bank-home-filter',
                    options=[{'label': 'All', 'value': 'all'}] + 
                            [{'label': h, 'value': h} for h in sorted(bank_df['home_ownership'].unique())],
                    value='all',
                    style={'backgroundColor': COLORS['card']}
                )
            ], md=3),
        ], style={'marginBottom': '30px'}),
        
        # KPI Row
        dbc.Row([
            dbc.Col(create_kpi_card("Total Applications", f"{total_applications:,}", 
                                    "fa-file-alt", COLORS['primary'], 
                                    delta=((mtd_applications/total_applications)*100), delta_text="MTD"), md=2),
            dbc.Col(create_kpi_card("Total Funded", f"₹{total_funded/1e6:.1f}M", 
                                    "fa-money-bill-wave", COLORS['success']), md=2),
            dbc.Col(create_kpi_card("Total Received", f"₹{total_received/1e6:.1f}M", 
                                    "fa-hand-holding-usd", COLORS['info']), md=2),
            dbc.Col(create_kpi_card("Avg Interest Rate", f"{avg_interest_rate:.1f}%", 
                                    "fa-percentage", COLORS['warning']), md=2),
            dbc.Col(create_kpi_card("Good Loans", f"{good_loan_pct:.1f}%", 
                                    "fa-check-circle", COLORS['success']), md=2),
            dbc.Col(create_kpi_card("Bad Loans", f"{bad_loan_pct:.1f}%", 
                                    "fa-times-circle", COLORS['danger']), md=2),
        ], style={'marginBottom': '20px'}),
        
        # Charts Row 1
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Monthly Funded Amount Trend", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='bank-monthly-funded-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=8),
            dbc.Col([
                html.Div([
                    html.H5("Loan Status Distribution", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='bank-loan-status-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=4),
        ]),
        
        # Charts Row 2
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Funded Amount by State", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='bank-state-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=6),
            dbc.Col([
                html.Div([
                    html.H5("Loan Purpose Breakdown", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='bank-purpose-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=6),
        ]),
        
        # Charts Row 3
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Term Distribution", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='bank-term-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=4),
            dbc.Col([
                html.Div([
                    html.H5("Employment Length Analysis", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='bank-emp-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=4),
            dbc.Col([
                html.Div([
                    html.H5("Home Ownership", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='bank-home-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=4),
        ]),
    ])

# ======================== BLINKIT DASHBOARD ========================

def create_blinkit_dashboard():
    """Create Blinkit Sales Analysis Dashboard"""
    if blinkit_df is None:
        return html.Div("Error loading Blinkit data", style={'color': 'red', 'textAlign': 'center', 'padding': '50px'})
    
    # Calculate KPIs
    total_sales = blinkit_df['Sales'].sum()
    avg_sales = blinkit_df['Sales'].mean()
    total_items = len(blinkit_df)
    avg_rating = blinkit_df['Rating'].mean()
    
    return html.Div([
        # Filters Row
        dbc.Row([
            dbc.Col([
                html.Label("Outlet Location", style={'color': COLORS['light'], 'marginBottom': '5px'}),
                dcc.Dropdown(
                    id='blinkit-location-filter',
                    options=[{'label': 'All Locations', 'value': 'all'}] + 
                            [{'label': l, 'value': l} for l in sorted(blinkit_df['Outlet Location Type'].unique())],
                    value='all',
                    style={'backgroundColor': COLORS['card']}
                )
            ], md=3),
            dbc.Col([
                html.Label("Outlet Size", style={'color': COLORS['light'], 'marginBottom': '5px'}),
                dcc.Dropdown(
                    id='blinkit-size-filter',
                    options=[{'label': 'All Sizes', 'value': 'all'}] + 
                            [{'label': s, 'value': s} for s in sorted(blinkit_df['Outlet Size'].dropna().unique())],
                    value='all',
                    style={'backgroundColor': COLORS['card']}
                )
            ], md=3),
            dbc.Col([
                html.Label("Item Type", style={'color': COLORS['light'], 'marginBottom': '5px'}),
                dcc.Dropdown(
                    id='blinkit-item-filter',
                    options=[{'label': 'All Items', 'value': 'all'}] + 
                            [{'label': t, 'value': t} for t in sorted(blinkit_df['Item Type'].unique())],
                    value='all',
                    style={'backgroundColor': COLORS['card']}
                )
            ], md=3),
            dbc.Col([
                html.Label("Fat Content", style={'color': COLORS['light'], 'marginBottom': '5px'}),
                dcc.Dropdown(
                    id='blinkit-fat-filter',
                    options=[{'label': 'All', 'value': 'all'}] + 
                            [{'label': f, 'value': f} for f in sorted(blinkit_df['Item Fat Content'].unique())],
                    value='all',
                    style={'backgroundColor': COLORS['card']}
                )
            ], md=3),
        ], style={'marginBottom': '30px'}),
        
        # KPI Row
        dbc.Row([
            dbc.Col(create_kpi_card("Total Sales", f"₹{total_sales:,.0f}", 
                                    "fa-rupee-sign", COLORS['success']), md=3),
            dbc.Col(create_kpi_card("Average Sales", f"₹{avg_sales:,.2f}", 
                                    "fa-chart-bar", COLORS['primary']), md=3),
            dbc.Col(create_kpi_card("Items Sold", f"{total_items:,}", 
                                    "fa-shopping-cart", COLORS['info']), md=3),
            dbc.Col(create_kpi_card("Avg Rating", f"{avg_rating:.1f} ⭐", 
                                    "fa-star", COLORS['warning']), md=3),
        ], style={'marginBottom': '20px'}),
        
        # Charts Row 1
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Sales by Item Type", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='blinkit-item-type-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=8),
            dbc.Col([
                html.Div([
                    html.H5("Sales by Fat Content", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='blinkit-fat-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=4),
        ]),
        
        # Charts Row 2
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Sales by Outlet Establishment Year", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='blinkit-year-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=6),
            dbc.Col([
                html.Div([
                    html.H5("Fat Content by Outlet Location", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='blinkit-fat-location-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=6),
        ]),
        
        # Charts Row 3
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Sales by Outlet Size", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='blinkit-size-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=4),
            dbc.Col([
                html.Div([
                    html.H5("Sales by Outlet Type", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='blinkit-outlet-type-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=4),
            dbc.Col([
                html.Div([
                    html.H5("Sales by Outlet Location", style={'color': 'white', 'marginBottom': '20px'}),
                    dcc.Graph(id='blinkit-location-chart', config={'displayModeBar': False})
                ], style=CARD_STYLE)
            ], md=4),
        ]),
    ])

# ======================== MAIN LAYOUT ========================

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container([
        html.Div(id='page-content')
    ], fluid=True, style={'padding': '0 30px'})
], style={'backgroundColor': COLORS['background'], 'minHeight': '100vh'})

# ======================== CALLBACKS ========================

@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/blinkit':
        return create_blinkit_dashboard()
    else:
        return create_bank_loan_dashboard()

@callback(
    Output('nav-bank', 'active'),
    Output('nav-blinkit', 'active'),
    Input('url', 'pathname')
)
def update_nav_active(pathname):
    if pathname == '/blinkit':
        return False, True
    return True, False

# ======================== BANK LOAN CALLBACKS ========================

@callback(
    Output('bank-monthly-funded-chart', 'figure'),
    Output('bank-loan-status-chart', 'figure'),
    Output('bank-state-chart', 'figure'),
    Output('bank-purpose-chart', 'figure'),
    Output('bank-term-chart', 'figure'),
    Output('bank-emp-chart', 'figure'),
    Output('bank-home-chart', 'figure'),
    Input('bank-state-filter', 'value'),
    Input('bank-purpose-filter', 'value'),
    Input('bank-term-filter', 'value'),
    Input('bank-home-filter', 'value')
)
def update_bank_charts(state, purpose, term, home):
    df = bank_df.copy()
    
    # Apply filters
    if state != 'all':
        df = df[df['address_state'] == state]
    if purpose != 'all':
        df = df[df['purpose'] == purpose]
    if term != 'all':
        df = df[df['term'] == term]
    if home != 'all':
        df = df[df['home_ownership'] == home]
    
    # Monthly Funded Chart
    monthly_funded = (
        df.sort_values('issue_date')
        .groupby('month_name', sort=False)['loan_amount']
        .sum()
        .div(1000000)
        .reset_index(name='amount')
    )
    monthly_funded_fig = go.Figure()
    monthly_funded_fig.add_trace(go.Scatter(
        x=monthly_funded['month_name'], y=monthly_funded['amount'],
        fill='tozeroy', mode='lines+markers',
        line=dict(color=COLORS['primary'], width=2),
        fillcolor='rgba(52, 152, 219, 0.3)',
        hovertemplate='<b>%{x}</b><br>₹%{y:.2f}M<extra></extra>'
    ))
    monthly_funded_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=20, t=20, b=60), height=300,
        xaxis=dict(tickangle=45, gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(title='Amount (₹ Millions)', gridcolor='rgba(255,255,255,0.1)')
    )
    
    # Loan Status Donut
    status_counts = df['loan_status'].value_counts()
    status_fig = go.Figure(data=[go.Pie(
        labels=status_counts.index, values=status_counts.values,
        hole=0.6, marker=dict(colors=[COLORS['success'], COLORS['danger'], COLORS['warning']]),
        textinfo='percent+label', textposition='outside',
        hovertemplate='<b>%{label}</b><br>Count: %{value:,}<br>%{percent}<extra></extra>'
    )])
    status_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20), height=300, showlegend=False
    )
    
    # State Chart
    state_funding = df.groupby('address_state')['loan_amount'].sum().sort_values(ascending=True).tail(15) / 1000000
    state_fig = go.Figure(data=[go.Bar(
        y=state_funding.index, x=state_funding.values,
        orientation='h', marker=dict(color=COLORS['info']),
        hovertemplate='<b>%{y}</b><br>₹%{x:.2f}M<extra></extra>'
    )])
    state_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=60, r=20, t=20, b=40), height=350,
        xaxis=dict(title='Amount (₹ Millions)', gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)')
    )
    
    # Purpose Chart
    purpose_funding = df.groupby('purpose')['loan_amount'].sum().sort_values(ascending=True) / 1000000
    purpose_fig = go.Figure(data=[go.Bar(
        y=purpose_funding.index, x=purpose_funding.values,
        orientation='h', marker=dict(color=COLORS['warning']),
        hovertemplate='<b>%{y}</b><br>₹%{x:.2f}M<extra></extra>'
    )])
    purpose_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=120, r=20, t=20, b=40), height=350,
        xaxis=dict(title='Amount (₹ Millions)', gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)')
    )
    
    # Term Donut
    term_funding = df.groupby('term')['loan_amount'].sum() / 1000000
    term_fig = go.Figure(data=[go.Pie(
        labels=term_funding.index, values=term_funding.values,
        hole=0.5, marker=dict(colors=[COLORS['primary'], COLORS['success']]),
        textinfo='percent+label', textposition='inside',
        hovertemplate='<b>%{label}</b><br>₹%{value:.2f}M<br>%{percent}<extra></extra>'
    )])
    term_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20), height=280, showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=-0.1, xanchor='center', x=0.5)
    )
    
    # Employment Chart
    emp_funding = df.groupby('emp_length')['loan_amount'].sum().sort_values(ascending=True) / 1000
    emp_fig = go.Figure(data=[go.Bar(
        y=emp_funding.index, x=emp_funding.values,
        orientation='h', marker=dict(color='#9b59b6'),
        hovertemplate='<b>%{y}</b><br>₹%{x:,.0f}K<extra></extra>'
    )])
    emp_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=80, r=20, t=20, b=40), height=280,
        xaxis=dict(title='Amount (₹ Thousands)', gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)')
    )
    
    # Home Ownership Treemap
    home_funding = df.groupby('home_ownership')['loan_amount'].sum().reset_index()
    home_funding['amount_millions'] = home_funding['loan_amount'] / 1000000
    home_fig = px.treemap(
        home_funding, path=['home_ownership'], values='amount_millions',
        color='amount_millions', color_continuous_scale='Blues',
        hover_data={'amount_millions': ':.2f'}
    )
    home_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=10), height=280, coloraxis_showscale=False
    )
    home_fig.update_traces(
        hovertemplate='<b>%{label}</b><br>₹%{value:.2f}M<extra></extra>'
    )
    
    return monthly_funded_fig, status_fig, state_fig, purpose_fig, term_fig, emp_fig, home_fig

# ======================== BLINKIT CALLBACKS ========================

@callback(
    Output('blinkit-item-type-chart', 'figure'),
    Output('blinkit-fat-chart', 'figure'),
    Output('blinkit-year-chart', 'figure'),
    Output('blinkit-fat-location-chart', 'figure'),
    Output('blinkit-size-chart', 'figure'),
    Output('blinkit-outlet-type-chart', 'figure'),
    Output('blinkit-location-chart', 'figure'),
    Input('blinkit-location-filter', 'value'),
    Input('blinkit-size-filter', 'value'),
    Input('blinkit-item-filter', 'value'),
    Input('blinkit-fat-filter', 'value')
)
def update_blinkit_charts(location, size, item_type, fat):
    df = blinkit_df.copy()
    
    # Apply filters
    if location != 'all':
        df = df[df['Outlet Location Type'] == location]
    if size != 'all':
        df = df[df['Outlet Size'] == size]
    if item_type != 'all':
        df = df[df['Item Type'] == item_type]
    if fat != 'all':
        df = df[df['Item Fat Content'] == fat]
    
    # Item Type Chart
    item_sales = df.groupby('Item Type')['Sales'].sum().sort_values(ascending=True)
    item_fig = go.Figure(data=[go.Bar(
        y=item_sales.index, x=item_sales.values,
        orientation='h', marker=dict(color=COLORS['primary']),
        hovertemplate='<b>%{y}</b><br>₹%{x:,.0f}<extra></extra>'
    )])
    item_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=140, r=20, t=20, b=40), height=400,
        xaxis=dict(title='Sales (₹)', gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)')
    )
    
    # Fat Content Pie
    fat_sales = df.groupby('Item Fat Content')['Sales'].sum()
    fat_fig = go.Figure(data=[go.Pie(
        labels=fat_sales.index, values=fat_sales.values,
        hole=0.5, marker=dict(colors=[COLORS['success'], COLORS['warning']]),
        textinfo='percent+label', textposition='inside',
        hovertemplate='<b>%{label}</b><br>₹%{value:,.0f}<br>%{percent}<extra></extra>'
    )])
    fat_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20), height=400, showlegend=False
    )
    
    # Year Line Chart
    year_sales = df.groupby('Outlet Establishment Year')['Sales'].sum().reset_index()
    year_fig = go.Figure(data=[go.Scatter(
        x=year_sales['Outlet Establishment Year'], y=year_sales['Sales'],
        mode='lines+markers', line=dict(color=COLORS['info'], width=3),
        marker=dict(size=10),
        hovertemplate='<b>%{x}</b><br>₹%{y:,.0f}<extra></extra>'
    )])
    year_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=20, t=20, b=40), height=300,
        xaxis=dict(title='Establishment Year', gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(title='Sales (₹)', gridcolor='rgba(255,255,255,0.1)')
    )
    
    # Fat by Location Grouped Bar
    fat_location = df.groupby(['Outlet Location Type', 'Item Fat Content'])['Sales'].sum().unstack(fill_value=0)
    fat_location_fig = go.Figure()
    for fat_type in fat_location.columns:
        fat_location_fig.add_trace(go.Bar(
            x=fat_location.index, y=fat_location[fat_type],
            name=fat_type, hovertemplate='<b>%{x}</b><br>' + fat_type + '<br>₹%{y:,.0f}<extra></extra>'
        ))
    fat_location_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=20, t=20, b=40), height=300, barmode='group',
        xaxis=dict(title='Location Tier', gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(title='Sales (₹)', gridcolor='rgba(255,255,255,0.1)'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    
    # Outlet Size Donut
    size_sales = df.groupby('Outlet Size')['Sales'].sum()
    size_fig = go.Figure(data=[go.Pie(
        labels=size_sales.index, values=size_sales.values,
        hole=0.6, marker=dict(colors=[COLORS['primary'], COLORS['success'], COLORS['warning']]),
        textinfo='percent+label', textposition='outside',
        hovertemplate='<b>%{label}</b><br>₹%{value:,.0f}<br>%{percent}<extra></extra>'
    )])
    size_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20), height=280, showlegend=False
    )
    
    # Outlet Type Bar
    outlet_sales = df.groupby('Outlet Type')['Sales'].sum().sort_values(ascending=True)
    outlet_fig = go.Figure(data=[go.Bar(
        y=outlet_sales.index, x=outlet_sales.values,
        orientation='h', marker=dict(color='#e74c3c'),
        hovertemplate='<b>%{y}</b><br>₹%{x:,.0f}<extra></extra>'
    )])
    outlet_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=120, r=20, t=20, b=40), height=280,
        xaxis=dict(title='Sales (₹)', gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)')
    )
    
    # Location Bar
    location_sales = df.groupby('Outlet Location Type')['Sales'].sum().sort_values(ascending=True)
    location_fig = go.Figure(data=[go.Bar(
        y=location_sales.index, x=location_sales.values,
        orientation='h', marker=dict(color='#9b59b6'),
        hovertemplate='<b>%{y}</b><br>₹%{x:,.0f}<extra></extra>'
    )])
    location_fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=60, r=20, t=20, b=40), height=280,
        xaxis=dict(title='Sales (₹)', gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)')
    )
    
    return item_fig, fat_fig, year_fig, fat_location_fig, size_fig, outlet_fig, location_fig

# ======================== RUN SERVER ========================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("[*] Starting Analytics Dashboard...")
    print("="*60)
    print("\n[>] Dashboard URL: http://127.0.0.1:8050")
    print("\n[+] Features:")
    print("    - Bank Loan Analysis - /bank-loan")
    print("    - Blinkit Sales Analysis - /blinkit")
    print("\n[!] The dashboard is dynamic with filters like Power BI!")
    print("="*60 + "\n")
    app.run(debug=False, host='127.0.0.1', port=8050)
