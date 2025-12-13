import React, { useState, useEffect } from 'react';

// SnapDish Professional Prototype
// Typography: Staatliches (titles), Archivo (body)
// Colors: Teal #1E8A8A, Camel #C68E5D, Coral #E85D3C, Cream #E6DED3, Dark #0D0D0D

const COLORS = {
  bg: '#0D0D0D',
  bgCard: '#1A1A1A',
  primary: '#E85D3C',
  primaryHover: '#FF7B5F',
  secondary: '#C68E5D',
  accent: '#1E8A8A',
  cream: '#E6DED3',
  text: '#FFFFFF',
  textMuted: 'rgba(255,255,255,0.7)',
  success: '#4CAF50',
  border: 'rgba(255,255,255,0.15)'
};

// Logo Component (matching the uploaded logo)
const Logo = ({ size = 48 }) => (
  <div style={{
    width: size,
    height: size,
    background: COLORS.primary,
    borderRadius: 12,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    position: 'relative'
  }}>
    <svg width={size * 0.7} height={size * 0.7} viewBox="0 0 40 40" fill="none">
      {/* Camera viewfinder corners */}
      <path d="M4 12V6C4 4.89543 4.89543 4 6 4H12" stroke="white" strokeWidth="2.5" strokeLinecap="round"/>
      <path d="M28 4H34C35.1046 4 36 4.89543 36 6V12" stroke="white" strokeWidth="2.5" strokeLinecap="round"/>
      <path d="M36 28V34C36 35.1046 35.1046 36 34 36H28" stroke="white" strokeWidth="2.5" strokeLinecap="round"/>
      <path d="M12 36H6C4.89543 36 4 35.1046 4 34V28" stroke="white" strokeWidth="2.5" strokeLinecap="round"/>
      {/* Bowl */}
      <ellipse cx="20" cy="24" rx="11" ry="6" fill="white"/>
      <path d="M9 24C9 24 11 30 20 30C29 30 31 24 31 24" stroke="white" strokeWidth="2"/>
      {/* Food items */}
      <circle cx="15" cy="21" r="3" fill="#E85D3C"/>
      <circle cx="20" cy="19" r="3.5" fill="#1E8A8A"/>
      <circle cx="25" cy="21" r="3" fill="#C68E5D"/>
    </svg>
  </div>
);

// Icon Components
const HomeIcon = ({ active }) => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke={active ? COLORS.primary : COLORS.textMuted} strokeWidth="2">
    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
    <polyline points="9 22 9 12 15 12 15 22"/>
  </svg>
);

const CameraIcon = ({ active }) => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke={active ? COLORS.primary : COLORS.textMuted} strokeWidth="2">
    <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/>
    <circle cx="12" cy="13" r="4"/>
  </svg>
);

const StarIcon = ({ active }) => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill={active ? COLORS.primary : "none"} stroke={active ? COLORS.primary : COLORS.textMuted} strokeWidth="2">
    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
  </svg>
);

const UserIcon = ({ active }) => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke={active ? COLORS.primary : COLORS.textMuted} strokeWidth="2">
    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
    <circle cx="12" cy="7" r="4"/>
  </svg>
);

const MenuIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke={COLORS.textMuted} strokeWidth="2">
    <line x1="3" y1="6" x2="21" y2="6"/>
    <line x1="3" y1="12" x2="21" y2="12"/>
    <line x1="3" y1="18" x2="21" y2="18"/>
  </svg>
);

const CheckIcon = () => (
  <svg width="16" height="16" viewBox="0 0 16 16" fill={COLORS.success}>
    <rect width="16" height="16" rx="3"/>
    <path d="M4 8l3 3 5-6" stroke="white" strokeWidth="2" fill="none" strokeLinecap="round" strokeLinejoin="round"/>
  </svg>
);

const BackIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke={COLORS.text} strokeWidth="2">
    <path d="M19 12H5M12 19l-7-7 7-7"/>
  </svg>
);

const AISparkle = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill={COLORS.secondary}>
    <path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/>
  </svg>
);

// Button Component
const Button = ({ children, variant = 'primary', onClick, style = {}, disabled = false }) => {
  const [isHovered, setIsHovered] = useState(false);
  
  const baseStyle = {
    fontFamily: "'Archivo', sans-serif",
    fontSize: 14,
    fontWeight: 600,
    padding: '14px 28px',
    borderRadius: 25,
    cursor: disabled ? 'not-allowed' : 'pointer',
    transition: 'all 0.2s ease',
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
    border: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    opacity: disabled ? 0.5 : 1,
  };
  
  const variants = {
    primary: {
      background: isHovered ? COLORS.primaryHover : COLORS.primary,
      color: 'white',
      transform: isHovered ? 'scale(1.02)' : 'scale(1)',
    },
    secondary: {
      background: 'transparent',
      color: COLORS.secondary,
      border: `1px solid ${COLORS.secondary}`,
    },
    ghost: {
      background: 'transparent',
      color: COLORS.cream,
      border: `1px solid ${COLORS.border}`,
    }
  };
  
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      style={{ ...baseStyle, ...variants[variant], ...style }}
    >
      {children}
    </button>
  );
};

// Tag Component
const Tag = ({ children, color = COLORS.primary }) => (
  <span style={{
    fontFamily: "'Archivo', sans-serif",
    fontSize: 10,
    fontWeight: 600,
    padding: '4px 10px',
    borderRadius: 12,
    background: color,
    color: 'white',
    textTransform: 'uppercase',
    letterSpacing: '0.5px'
  }}>
    {children}
  </span>
);

// Navigation Bar Component
const NavBar = ({ currentPage, onNavigate }) => (
  <div style={{
    position: 'fixed',
    bottom: 0,
    left: '50%',
    transform: 'translateX(-50%)',
    width: 390,
    background: COLORS.bgCard,
    borderTop: `1px solid ${COLORS.border}`,
    padding: '12px 0 20px',
    display: 'flex',
    justifyContent: 'space-around',
    zIndex: 100
  }}>
    {[
      { id: 'home', icon: HomeIcon, label: 'Home' },
      { id: 'snap', icon: CameraIcon, label: 'Snap' },
      { id: 'plan', icon: StarIcon, label: 'Plan' },
      { id: 'profile', icon: UserIcon, label: 'Profile' }
    ].map(item => (
      <button
        key={item.id}
        onClick={() => onNavigate(item.id)}
        style={{
          background: 'none',
          border: 'none',
          cursor: 'pointer',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: 4,
          padding: 8
        }}
      >
        <item.icon active={currentPage === item.id} />
        <span style={{
          fontFamily: "'Archivo', sans-serif",
          fontSize: 10,
          color: currentPage === item.id ? COLORS.primary : COLORS.textMuted
        }}>
          {item.label}
        </span>
      </button>
    ))}
  </div>
);

// Header Component
const Header = ({ showBack, onBack, title }) => (
  <div style={{
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: '16px 20px',
    position: 'relative'
  }}>
    {showBack ? (
      <button onClick={onBack} style={{ background: 'none', border: 'none', cursor: 'pointer', padding: 4 }}>
        <BackIcon />
      </button>
    ) : (
      <button style={{ background: 'none', border: 'none', cursor: 'pointer', padding: 4 }}>
        <MenuIcon />
      </button>
    )}
    
    {title ? (
      <h2 style={{
        fontFamily: "'Staatliches', cursive",
        fontSize: 20,
        color: COLORS.secondary,
        margin: 0,
        letterSpacing: 1
      }}>{title}</h2>
    ) : (
      <Logo size={36} />
    )}
    
    <div style={{
      width: 36,
      height: 36,
      borderRadius: '50%',
      background: COLORS.secondary,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontFamily: "'Archivo', sans-serif",
      fontWeight: 700,
      fontSize: 12,
      color: COLORS.bg
    }}>
      YL
    </div>
  </div>
);

// Splash Screen
const SplashScreen = ({ onGetStarted, onLogin }) => {
  const [showContent, setShowContent] = useState(false);
  
  useEffect(() => {
    setTimeout(() => setShowContent(true), 300);
  }, []);
  
  return (
    <div style={{
      minHeight: '100%',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      padding: 40,
      opacity: showContent ? 1 : 0,
      transform: showContent ? 'translateY(0)' : 'translateY(20px)',
      transition: 'all 0.6s ease'
    }}>
      <div style={{ marginBottom: 24 }}>
        <Logo size={80} />
      </div>
      
      <h1 style={{
        fontFamily: "'Staatliches', cursive",
        fontSize: 48,
        color: COLORS.text,
        margin: 0,
        letterSpacing: 2,
        textAlign: 'center'
      }}>
        SNAPDISH
      </h1>
      
      <p style={{
        fontFamily: "'Archivo', sans-serif",
        fontSize: 16,
        color: COLORS.textMuted,
        textAlign: 'center',
        marginTop: 16,
        lineHeight: 1.5
      }}>
        One picture. One recipe.<br/>Zero thinking.
      </p>
      
      <div style={{ marginTop: 60, width: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 16 }}>
        <Button onClick={onGetStarted} style={{ width: '80%' }}>
          Get Started
        </Button>
        
        <button
          onClick={onLogin}
          style={{
            background: 'none',
            border: 'none',
            fontFamily: "'Archivo', sans-serif",
            fontSize: 14,
            color: COLORS.secondary,
            cursor: 'pointer',
            padding: 8,
            textDecoration: 'underline',
            textUnderlineOffset: 4
          }}
        >
          Log in
        </button>
      </div>
    </div>
  );
};

// Onboarding Screens
const OnboardingScreen = ({ step, totalSteps, title, children, onNext, onBack }) => (
  <div style={{ minHeight: '100%', padding: 24, display: 'flex', flexDirection: 'column' }}>
    <div style={{ display: 'flex', alignItems: 'center', gap: 16, marginBottom: 8 }}>
      {step > 1 && (
        <button onClick={onBack} style={{ background: 'none', border: 'none', cursor: 'pointer', padding: 4 }}>
          <BackIcon />
        </button>
      )}
      <span style={{
        fontFamily: "'Archivo', sans-serif",
        fontSize: 12,
        color: COLORS.secondary,
        textTransform: 'uppercase',
        letterSpacing: 1
      }}>
        Step {step}/{totalSteps}
      </span>
    </div>
    
    <h1 style={{
      fontFamily: "'Staatliches', cursive",
      fontSize: 36,
      color: COLORS.secondary,
      margin: '16px 0',
      letterSpacing: 1
    }}>
      {title}
    </h1>
    
    <div style={{ flex: 1 }}>
      {children}
    </div>
    
    <Button onClick={onNext} style={{ width: '100%', marginTop: 24 }}>
      {step === totalSteps ? 'Create Account' : 'Next'}
    </Button>
  </div>
);

// Checkbox Option Component
const CheckboxOption = ({ label, checked, onChange }) => (
  <button
    onClick={onChange}
    style={{
      display: 'flex',
      alignItems: 'center',
      gap: 12,
      padding: 16,
      background: checked ? 'rgba(232, 93, 60, 0.1)' : COLORS.bgCard,
      border: `1px solid ${checked ? COLORS.primary : COLORS.border}`,
      borderRadius: 12,
      cursor: 'pointer',
      width: '100%',
      textAlign: 'left'
    }}
  >
    <div style={{
      width: 24,
      height: 24,
      borderRadius: 6,
      border: `2px solid ${checked ? COLORS.primary : COLORS.border}`,
      background: checked ? COLORS.primary : 'transparent',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    }}>
      {checked && (
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
          <path d="M2 7l4 4 6-8" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
      )}
    </div>
    <span style={{
      fontFamily: "'Archivo', sans-serif",
      fontSize: 16,
      color: COLORS.text
    }}>
      {label}
    </span>
  </button>
);

// Home Screen
const HomeScreen = ({ onSnapFridge, onScanDish, onViewRecipe }) => {
  return (
    <div style={{ paddingBottom: 100 }}>
      <Header />
      
      <div style={{ padding: '0 20px' }}>
        <h2 style={{
          fontFamily: "'Staatliches', cursive",
          fontSize: 32,
          color: COLORS.secondary,
          margin: '8px 0 24px',
          display: 'flex',
          alignItems: 'center',
          gap: 8
        }}>
          HI YVETTE <span style={{ fontSize: 28 }}>👋</span>
        </h2>
        
        {/* Hungry Card */}
        <div style={{
          border: `2px dashed ${COLORS.border}`,
          borderRadius: 16,
          padding: 24,
          textAlign: 'center',
          marginBottom: 20
        }}>
          <h3 style={{
            fontFamily: "'Staatliches', cursive",
            fontSize: 28,
            color: COLORS.cream,
            margin: 0
          }}>
            hungry?
          </h3>
        </div>
        
        {/* Action Buttons */}
        <div style={{ display: 'flex', gap: 12, marginBottom: 32 }}>
          <Button onClick={onSnapFridge} style={{ flex: 1, fontSize: 12, padding: '14px 12px' }}>
            Snap My Fridge
          </Button>
          <Button onClick={onScanDish} style={{ flex: 1, fontSize: 12, padding: '14px 12px' }}>
            Scan A Dish
          </Button>
        </div>
        
        {/* Today's Picks */}
        <h3 style={{
          fontFamily: "'Staatliches', cursive",
          fontSize: 20,
          color: COLORS.secondary,
          margin: '0 0 16px',
          letterSpacing: 1
        }}>
          TODAY'S PICKS
        </h3>
        
        {/* Recipe Card */}
        <div
          onClick={onViewRecipe}
          style={{
            background: COLORS.bgCard,
            borderRadius: 16,
            overflow: 'hidden',
            cursor: 'pointer',
            transition: 'transform 0.2s ease'
          }}
        >
          <div style={{
            height: 140,
            background: 'linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%)',
            position: 'relative',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}>
            <span style={{ fontSize: 48 }}>🥗</span>
            <div style={{
              position: 'absolute',
              top: 12,
              right: 12,
              display: 'flex',
              alignItems: 'center',
              gap: 4,
              background: 'rgba(0,0,0,0.6)',
              padding: '4px 8px',
              borderRadius: 12
            }}>
              <AISparkle />
              <span style={{ fontFamily: "'Archivo', sans-serif", fontSize: 10, color: COLORS.secondary }}>AI Pick</span>
            </div>
          </div>
          
          <div style={{ padding: 16 }}>
            <h4 style={{
              fontFamily: "'Archivo', sans-serif",
              fontSize: 18,
              fontWeight: 600,
              color: COLORS.text,
              margin: '0 0 8px'
            }}>
              Spicy Tofu Bowl
            </h4>
            
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <div style={{ display: 'flex', gap: 6 }}>
                <Tag color={COLORS.accent}>High Protein</Tag>
                <Tag color={COLORS.secondary}>Budget</Tag>
                <Tag color={COLORS.success}>Vegetarian</Tag>
              </div>
              <span style={{
                fontFamily: "'Archivo', sans-serif",
                fontSize: 14,
                fontWeight: 600,
                color: COLORS.primary
              }}>
                15 min
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Snap/Camera Screen
const SnapScreen = ({ mode, onCapture, onBack }) => {
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  
  const handleCapture = () => {
    setIsAnalyzing(true);
    setTimeout(() => {
      setIsAnalyzing(false);
      onCapture();
    }, 2000);
  };
  
  return (
    <div style={{ minHeight: '100%', display: 'flex', flexDirection: 'column' }}>
      <Header showBack onBack={onBack} title={mode === 'fridge' ? 'SNAP FRIDGE' : 'SCAN DISH'} />
      
      <div style={{ flex: 1, padding: 20, display: 'flex', flexDirection: 'column' }}>
        {/* Camera Viewfinder */}
        <div style={{
          flex: 1,
          background: '#000',
          borderRadius: 24,
          position: 'relative',
          overflow: 'hidden',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          minHeight: 400
        }}>
          {/* Corner brackets */}
          <div style={{ position: 'absolute', top: 20, left: 20, width: 40, height: 40, borderLeft: `3px solid ${COLORS.primary}`, borderTop: `3px solid ${COLORS.primary}` }} />
          <div style={{ position: 'absolute', top: 20, right: 20, width: 40, height: 40, borderRight: `3px solid ${COLORS.primary}`, borderTop: `3px solid ${COLORS.primary}` }} />
          <div style={{ position: 'absolute', bottom: 20, left: 20, width: 40, height: 40, borderLeft: `3px solid ${COLORS.primary}`, borderBottom: `3px solid ${COLORS.primary}` }} />
          <div style={{ position: 'absolute', bottom: 20, right: 20, width: 40, height: 40, borderRight: `3px solid ${COLORS.primary}`, borderBottom: `3px solid ${COLORS.primary}` }} />
          
          {isAnalyzing ? (
            <div style={{ textAlign: 'center' }}>
              <div style={{
                width: 60,
                height: 60,
                border: `3px solid ${COLORS.primary}`,
                borderTopColor: 'transparent',
                borderRadius: '50%',
                animation: 'spin 1s linear infinite',
                margin: '0 auto 16px'
              }} />
              <p style={{
                fontFamily: "'Archivo', sans-serif",
                fontSize: 16,
                color: COLORS.text,
                display: 'flex',
                alignItems: 'center',
                gap: 8
              }}>
                <AISparkle /> AI Analyzing...
              </p>
            </div>
          ) : (
            <p style={{
              fontFamily: "'Archivo', sans-serif",
              fontSize: 16,
              color: COLORS.textMuted,
              textAlign: 'center'
            }}>
              Point camera at your {mode === 'fridge' ? 'fridge' : 'dish'}
            </p>
          )}
        </div>
        
        {/* Capture Button */}
        <div style={{ display: 'flex', justifyContent: 'center', padding: '24px 0' }}>
          <button
            onClick={handleCapture}
            disabled={isAnalyzing}
            style={{
              width: 72,
              height: 72,
              borderRadius: '50%',
              background: 'transparent',
              border: `4px solid ${COLORS.primary}`,
              cursor: isAnalyzing ? 'not-allowed' : 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              transition: 'all 0.2s ease'
            }}
          >
            <div style={{
              width: 56,
              height: 56,
              borderRadius: '50%',
              background: COLORS.primary,
              transition: 'transform 0.1s ease'
            }} />
          </button>
        </div>
      </div>
      
      <style>{`
        @keyframes spin {
          to { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
};

// Ingredients Result Screen
const IngredientsScreen = ({ onSeeRecipes, onBack }) => {
  const ingredients = [
    { name: 'Eggs', have: true },
    { name: 'Spinach', have: true },
    { name: 'Tomatoes', have: true },
    { name: 'Cheese', have: true },
    { name: 'Onion', have: true }
  ];
  
  return (
    <div style={{ minHeight: '100%', paddingBottom: 100 }}>
      <Header showBack onBack={onBack} title="WE FOUND" />
      
      <div style={{ padding: '0 20px' }}>
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: 8,
          marginBottom: 24
        }}>
          <AISparkle />
          <span style={{
            fontFamily: "'Archivo', sans-serif",
            fontSize: 14,
            color: COLORS.secondary
          }}>
            AI detected {ingredients.length} ingredients
          </span>
        </div>
        
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10, marginBottom: 32 }}>
          {ingredients.map((item, i) => (
            <div
              key={i}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 8,
                background: COLORS.bgCard,
                padding: '10px 16px',
                borderRadius: 20,
                border: `1px solid ${COLORS.success}`
              }}
            >
              <CheckIcon />
              <span style={{
                fontFamily: "'Archivo', sans-serif",
                fontSize: 14,
                color: COLORS.text
              }}>
                {item.name}
              </span>
            </div>
          ))}
        </div>
        
        <Button onClick={onSeeRecipes} style={{ width: '100%' }}>
          See AI Recipes
        </Button>
      </div>
    </div>
  );
};

// Recipe Detail Screen
const RecipeScreen = ({ onBack, onCook }) => {
  const ingredients = [
    { name: 'Eggs', have: true },
    { name: 'Spinach', have: true },
    { name: 'Tomatoes', have: true },
    { name: 'Cheese', have: true },
    { name: 'Onion', have: true }
  ];
  
  const steps = [
    'Whisk eggs in a bowl with salt and pepper',
    'Chop spinach, tomatoes, and onion',
    'Heat pan with olive oil over medium heat',
    'Pour eggs and add vegetables when edges set'
  ];
  
  return (
    <div style={{ minHeight: '100%', paddingBottom: 100 }}>
      {/* Hero Image */}
      <div style={{
        height: 220,
        background: 'linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(13,13,13,1) 100%), linear-gradient(135deg, #3a3a3a 0%, #1a1a1a 100%)',
        position: 'relative',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center'
      }}>
        <span style={{ fontSize: 80 }}>🍳</span>
        <button
          onClick={onBack}
          style={{
            position: 'absolute',
            top: 16,
            left: 16,
            background: 'rgba(0,0,0,0.5)',
            border: 'none',
            borderRadius: '50%',
            width: 40,
            height: 40,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}
        >
          <BackIcon />
        </button>
      </div>
      
      <div style={{ padding: '0 20px' }}>
        <h1 style={{
          fontFamily: "'Staatliches', cursive",
          fontSize: 32,
          color: COLORS.secondary,
          margin: '16px 0 8px',
          letterSpacing: 1
        }}>
          MEDITERRANEAN OMELETTE
        </h1>
        
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: 8,
          marginBottom: 24
        }}>
          <AISparkle />
          <span style={{ fontFamily: "'Archivo', sans-serif", fontSize: 14, color: COLORS.textMuted }}>
            AI Generated Recipe
          </span>
        </div>
        
        {/* Ingredients */}
        <h3 style={{
          fontFamily: "'Staatliches', cursive",
          fontSize: 18,
          color: COLORS.secondary,
          margin: '0 0 12px',
          letterSpacing: 1
        }}>
          INGREDIENTS
        </h3>
        
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginBottom: 20 }}>
          {ingredients.map((item, i) => (
            <div
              key={i}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 6,
                background: COLORS.bgCard,
                padding: '8px 12px',
                borderRadius: 16
              }}
            >
              <CheckIcon />
              <span style={{
                fontFamily: "'Archivo', sans-serif",
                fontSize: 13,
                color: COLORS.text
              }}>
                {item.name}
              </span>
            </div>
          ))}
        </div>
        
        <Button onClick={onCook} style={{ width: '100%', marginBottom: 24 }}>
          Cook This
        </Button>
        
        {/* Steps */}
        <h3 style={{
          fontFamily: "'Staatliches', cursive",
          fontSize: 18,
          color: COLORS.secondary,
          margin: '0 0 12px',
          letterSpacing: 1
        }}>
          STEPS
        </h3>
        
        {steps.map((step, i) => (
          <div
            key={i}
            style={{
              display: 'flex',
              gap: 12,
              marginBottom: 12,
              padding: 12,
              background: COLORS.bgCard,
              borderRadius: 12
            }}
          >
            <span style={{
              fontFamily: "'Staatliches', cursive",
              fontSize: 20,
              color: COLORS.primary,
              minWidth: 24
            }}>
              {i + 1}.
            </span>
            <p style={{
              fontFamily: "'Archivo', sans-serif",
              fontSize: 14,
              color: COLORS.text,
              margin: 0,
              lineHeight: 1.5
            }}>
              {step}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

// Cooking Guide Screen
const CookingScreen = ({ onFinish, onBack }) => {
  const [currentStep, setCurrentStep] = useState(1);
  const totalSteps = 4;
  
  const steps = [
    { title: 'WHISK', subtitle: 'THE EGGS', detail: 'Beat eggs with salt and pepper until fluffy' },
    { title: 'CHOP', subtitle: 'THE VEGGIES', detail: 'Dice tomatoes, spinach, and onion' },
    { title: 'HEAT', subtitle: 'THE PAN', detail: 'Medium heat with a drizzle of olive oil' },
    { title: 'COOK', subtitle: 'YOUR OMELETTE', detail: 'Pour eggs, add veggies, fold when set' }
  ];
  
  const handleNext = () => {
    if (currentStep < totalSteps) {
      setCurrentStep(currentStep + 1);
    } else {
      onFinish();
    }
  };
  
  return (
    <div style={{ minHeight: '100%', display: 'flex', flexDirection: 'column' }}>
      <Header showBack onBack={onBack} title={`STEP ${currentStep}/${totalSteps}`} />
      
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: 40 }}>
        <h1 style={{
          fontFamily: "'Staatliches', cursive",
          fontSize: 56,
          color: COLORS.primary,
          margin: 0,
          textAlign: 'center',
          lineHeight: 1
        }}>
          {steps[currentStep - 1].title}
        </h1>
        <h2 style={{
          fontFamily: "'Staatliches', cursive",
          fontSize: 40,
          color: COLORS.secondary,
          margin: '8px 0 24px',
          textAlign: 'center'
        }}>
          {steps[currentStep - 1].subtitle}
        </h2>
        <p style={{
          fontFamily: "'Archivo', sans-serif",
          fontSize: 16,
          color: COLORS.textMuted,
          textAlign: 'center'
        }}>
          {steps[currentStep - 1].detail}
        </p>
      </div>
      
      {/* Progress dots */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: 8, marginBottom: 16 }}>
        {Array.from({ length: totalSteps }).map((_, i) => (
          <div
            key={i}
            style={{
              width: i + 1 === currentStep ? 24 : 8,
              height: 8,
              borderRadius: 4,
              background: i + 1 <= currentStep ? COLORS.primary : COLORS.border,
              transition: 'all 0.3s ease'
            }}
          />
        ))}
      </div>
      
      <div style={{ padding: 20 }}>
        <Button onClick={handleNext} style={{ width: '100%' }}>
          {currentStep === totalSteps ? 'Finish Cooking' : 'Next Step'}
        </Button>
      </div>
    </div>
  );
};

// Monthly Plan Screen
const PlanScreen = ({ isPremium }) => {
  return (
    <div style={{ minHeight: '100%', paddingBottom: 100 }}>
      <Header title="MONTHLY PLAN" />
      
      <div style={{ padding: '0 20px' }}>
        {/* Premium Upsell Card */}
        <div style={{
          background: `linear-gradient(135deg, ${COLORS.primary} 0%, ${COLORS.secondary} 100%)`,
          borderRadius: 20,
          padding: 3,
          marginBottom: 24
        }}>
          <div style={{
            background: COLORS.bg,
            borderRadius: 17,
            padding: 24,
            textAlign: 'center'
          }}>
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: 8,
              marginBottom: 12
            }}>
              <AISparkle />
              <h3 style={{
                fontFamily: "'Staatliches', cursive",
                fontSize: 24,
                color: COLORS.secondary,
                margin: 0
              }}>
                UNLOCK AI PLANNER
              </h3>
            </div>
            
            <p style={{
              fontFamily: "'Archivo', sans-serif",
              fontSize: 14,
              color: COLORS.textMuted,
              margin: '0 0 16px'
            }}>
              Get AI-generated zero-waste meal plans<br/>
              Upgrade your eating experience
            </p>
            
            <h2 style={{
              fontFamily: "'Staatliches', cursive",
              fontSize: 40,
              color: COLORS.primary,
              margin: '0 0 20px'
            }}>
              $7.99/MO
            </h2>
            
            <div style={{ display: 'flex', gap: 12 }}>
              <Button style={{ flex: 1 }}>
                Start Free Trial
              </Button>
              <Button variant="secondary" style={{ flex: 1 }}>
                View Benefits
              </Button>
            </div>
          </div>
        </div>
        
        {/* Features List */}
        <h3 style={{
          fontFamily: "'Staatliches', cursive",
          fontSize: 18,
          color: COLORS.secondary,
          margin: '0 0 16px'
        }}>
          PREMIUM FEATURES
        </h3>
        
        {[
          'Unlimited AI recipe generations',
          'Save recipes to your collection',
          'Weekly AI meal planning',
          'Smart grocery lists',
          'Nutrition tracking & macros',
          'Priority support'
        ].map((feature, i) => (
          <div
            key={i}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 12,
              padding: 16,
              background: COLORS.bgCard,
              borderRadius: 12,
              marginBottom: 8
            }}
          >
            <CheckIcon />
            <span style={{
              fontFamily: "'Archivo', sans-serif",
              fontSize: 14,
              color: COLORS.text
            }}>
              {feature}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

// Profile Screen
const ProfileScreen = ({ onLogout }) => {
  return (
    <div style={{ minHeight: '100%', paddingBottom: 100 }}>
      <Header title="PROFILE" />
      
      <div style={{ padding: '0 20px' }}>
        {/* Profile Card */}
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: 16,
          padding: 20,
          background: COLORS.bgCard,
          borderRadius: 16,
          marginBottom: 24
        }}>
          <div style={{
            width: 64,
            height: 64,
            borderRadius: '50%',
            background: COLORS.secondary,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontFamily: "'Archivo', sans-serif",
            fontWeight: 700,
            fontSize: 24,
            color: COLORS.bg
          }}>
            YL
          </div>
          
          <div>
            <h3 style={{
              fontFamily: "'Archivo', sans-serif",
              fontSize: 20,
              fontWeight: 600,
              color: COLORS.text,
              margin: 0
            }}>
              Yvette Luo
            </h3>
            <p style={{
              fontFamily: "'Archivo', sans-serif",
              fontSize: 14,
              color: COLORS.textMuted,
              margin: '4px 0 0'
            }}>
              Free Plan · 3 recipes saved
            </p>
          </div>
        </div>
        
        {/* Menu Items */}
        {[
          { icon: '🍽️', label: 'Dietary Preferences' },
          { icon: '📖', label: 'Saved Recipes' },
          { icon: '⭐', label: 'Upgrade to Premium' },
          { icon: '🔔', label: 'Notifications' },
          { icon: '❓', label: 'Help & Support' }
        ].map((item, i) => (
          <button
            key={i}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 16,
              width: '100%',
              padding: 16,
              background: COLORS.bgCard,
              border: 'none',
              borderRadius: 12,
              marginBottom: 8,
              cursor: 'pointer',
              textAlign: 'left'
            }}
          >
            <span style={{ fontSize: 20 }}>{item.icon}</span>
            <span style={{
              fontFamily: "'Archivo', sans-serif",
              fontSize: 16,
              color: COLORS.text
            }}>
              {item.label}
            </span>
          </button>
        ))}
        
        <button
          onClick={onLogout}
          style={{
            width: '100%',
            padding: 16,
            background: 'transparent',
            border: `1px solid ${COLORS.primary}`,
            borderRadius: 12,
            cursor: 'pointer',
            marginTop: 16
          }}
        >
          <span style={{
            fontFamily: "'Archivo', sans-serif",
            fontSize: 16,
            color: COLORS.primary
          }}>
            Log Out
          </span>
        </button>
      </div>
    </div>
  );
};

// Main App Component
export default function SnapDishApp() {
  const [currentPage, setCurrentPage] = useState('splash');
  const [onboardingStep, setOnboardingStep] = useState(1);
  const [goals, setGoals] = useState([]);
  const [snapMode, setSnapMode] = useState(null);
  
  const navigate = (page) => setCurrentPage(page);
  
  const handleNavigation = (page) => {
    if (page === 'snap') {
      setSnapMode('fridge');
      setCurrentPage('snap');
    } else {
      setCurrentPage(page);
    }
  };
  
  const showNavBar = ['home', 'plan', 'profile'].includes(currentPage);
  
  const goalOptions = [
    'Reduce food waste',
    'Decide what to cook',
    'Eat healthier',
    'Save time'
  ];
  
  return (
    <div style={{
      width: 390,
      minHeight: 844,
      maxHeight: 844,
      margin: '20px auto',
      background: COLORS.bg,
      borderRadius: 40,
      overflow: 'hidden',
      position: 'relative',
      boxShadow: '0 25px 50px -12px rgba(0,0,0,0.5)',
      border: '8px solid #222',
      fontFamily: "'Archivo', sans-serif"
    }}>
      {/* Dynamic Island */}
      <div style={{
        position: 'absolute',
        top: 12,
        left: '50%',
        transform: 'translateX(-50%)',
        width: 120,
        height: 32,
        background: '#000',
        borderRadius: 20,
        zIndex: 200
      }} />
      
      {/* Content Area */}
      <div style={{
        height: '100%',
        overflowY: 'auto',
        paddingTop: 48
      }}>
        {currentPage === 'splash' && (
          <SplashScreen
            onGetStarted={() => navigate('onboarding')}
            onLogin={() => navigate('home')}
          />
        )}
        
        {currentPage === 'onboarding' && onboardingStep === 1 && (
          <OnboardingScreen
            step={1}
            totalSteps={3}
            title="GOALS"
            onNext={() => setOnboardingStep(2)}
          >
            <p style={{
              fontFamily: "'Archivo', sans-serif",
              fontSize: 14,
              color: COLORS.textMuted,
              marginBottom: 20
            }}>
              What do you want SnapDish to help with?
            </p>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
              {goalOptions.map((goal, i) => (
                <CheckboxOption
                  key={i}
                  label={goal}
                  checked={goals.includes(goal)}
                  onChange={() => {
                    if (goals.includes(goal)) {
                      setGoals(goals.filter(g => g !== goal));
                    } else {
                      setGoals([...goals, goal]);
                    }
                  }}
                />
              ))}
            </div>
          </OnboardingScreen>
        )}
        
        {currentPage === 'onboarding' && onboardingStep === 2 && (
          <OnboardingScreen
            step={2}
            totalSteps={3}
            title="DIET & PREFS"
            onNext={() => setOnboardingStep(3)}
            onBack={() => setOnboardingStep(1)}
          >
            <div style={{ marginBottom: 20 }}>
              <label style={{
                fontFamily: "'Archivo', sans-serif",
                fontSize: 14,
                color: COLORS.textMuted,
                display: 'block',
                marginBottom: 8
              }}>
                I eat...
              </label>
              <select style={{
                width: '100%',
                padding: 16,
                background: COLORS.bgCard,
                border: `1px solid ${COLORS.border}`,
                borderRadius: 12,
                color: COLORS.text,
                fontFamily: "'Archivo', sans-serif",
                fontSize: 16
              }}>
                <option>Everything</option>
                <option>Vegetarian</option>
                <option>Vegan</option>
                <option>Pescatarian</option>
                <option>Halal</option>
                <option>Kosher</option>
              </select>
            </div>
            
            <div>
              <label style={{
                fontFamily: "'Archivo', sans-serif",
                fontSize: 14,
                color: COLORS.textMuted,
                display: 'block',
                marginBottom: 8
              }}>
                Allergies...
              </label>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
                {['Nuts', 'Dairy', 'Gluten', 'Shellfish', 'Eggs', 'Soy'].map((allergy, i) => (
                  <button
                    key={i}
                    style={{
                      padding: '10px 16px',
                      background: COLORS.bgCard,
                      border: `1px solid ${COLORS.border}`,
                      borderRadius: 20,
                      color: COLORS.text,
                      fontFamily: "'Archivo', sans-serif",
                      fontSize: 14,
                      cursor: 'pointer'
                    }}
                  >
                    {allergy}
                  </button>
                ))}
              </div>
            </div>
          </OnboardingScreen>
        )}
        
        {currentPage === 'onboarding' && onboardingStep === 3 && (
          <OnboardingScreen
            step={3}
            totalSteps={3}
            title="SKILL LEVEL"
            onNext={() => {
              setOnboardingStep(1);
              navigate('home');
            }}
            onBack={() => setOnboardingStep(2)}
          >
            <p style={{
              fontFamily: "'Archivo', sans-serif",
              fontSize: 14,
              color: COLORS.textMuted,
              marginBottom: 20
            }}>
              How comfortable are you in the kitchen?
            </p>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
              {['Beginner', 'Intermediate', 'Advanced'].map((level, i) => (
                <button
                  key={i}
                  style={{
                    padding: 20,
                    background: i === 1 ? 'rgba(232, 93, 60, 0.1)' : COLORS.bgCard,
                    border: `1px solid ${i === 1 ? COLORS.primary : COLORS.border}`,
                    borderRadius: 12,
                    color: COLORS.text,
                    fontFamily: "'Archivo', sans-serif",
                    fontSize: 16,
                    cursor: 'pointer',
                    textAlign: 'left'
                  }}
                >
                  {level}
                </button>
              ))}
            </div>
          </OnboardingScreen>
        )}
        
        {currentPage === 'home' && (
          <HomeScreen
            onSnapFridge={() => { setSnapMode('fridge'); navigate('snap'); }}
            onScanDish={() => { setSnapMode('dish'); navigate('snap'); }}
            onViewRecipe={() => navigate('recipe')}
          />
        )}
        
        {currentPage === 'snap' && (
          <SnapScreen
            mode={snapMode}
            onCapture={() => navigate('ingredients')}
            onBack={() => navigate('home')}
          />
        )}
        
        {currentPage === 'ingredients' && (
          <IngredientsScreen
            onSeeRecipes={() => navigate('recipe')}
            onBack={() => navigate('snap')}
          />
        )}
        
        {currentPage === 'recipe' && (
          <RecipeScreen
            onBack={() => navigate('home')}
            onCook={() => navigate('cooking')}
          />
        )}
        
        {currentPage === 'cooking' && (
          <CookingScreen
            onFinish={() => navigate('home')}
            onBack={() => navigate('recipe')}
          />
        )}
        
        {currentPage === 'plan' && (
          <PlanScreen isPremium={false} />
        )}
        
        {currentPage === 'profile' && (
          <ProfileScreen onLogout={() => navigate('splash')} />
        )}
      </div>
      
      {showNavBar && (
        <NavBar currentPage={currentPage} onNavigate={handleNavigation} />
      )}
      
      {/* Google Fonts Import */}
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Staatliches&family=Archivo:wght@400;500;600;700&display=swap');
        
        * {
          box-sizing: border-box;
          -webkit-font-smoothing: antialiased;
        }
        
        ::-webkit-scrollbar {
          display: none;
        }
        
        select option {
          background: ${COLORS.bgCard};
          color: ${COLORS.text};
        }
      `}</style>
    </div>
  );
}
