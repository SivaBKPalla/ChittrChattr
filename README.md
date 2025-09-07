# ChittrChattr - Where Conversations Come Alive

A full-featured social media application built with React, TypeScript, and Tailwind CSS. ChittrChattr is designed to foster meaningful conversations and connections in a modern, intuitive interface.

## 🚀 Features

### Core Features
- **User Authentication**: Secure login and registration system
- **User Profiles**: Complete user profiles with bio, avatar, cover image, and stats
- **Conversation Creation**: Rich text conversations with image support
- **Social Interactions**: Like, comment, share, and follow functionality
- **Responsive Design**: Beautiful, mobile-first UI that works on all devices
- **Real-time Updates**: Live notifications and updates

### User Interface
- **Modern Design**: Clean, intuitive interface with smooth animations
- **Dark/Light Mode**: Automatic theme switching based on system preferences
- **Mobile Responsive**: Optimized for mobile, tablet, and desktop
- **Accessibility**: Built with accessibility best practices

### Technical Features
- **TypeScript**: Full type safety throughout the application
- **React Hooks**: Modern React patterns with custom hooks
- **Context API**: Global state management for authentication
- **React Router**: Client-side routing with protected routes
- **Tailwind CSS**: Utility-first CSS framework for rapid styling

## 🛠️ Tech Stack

- **Frontend**: React 18, TypeScript, Tailwind CSS
- **Routing**: React Router DOM
- **Icons**: Lucide React
- **Date Handling**: date-fns
- **Build Tool**: Create React App

## 📦 Installation

### Prerequisites
- Node.js (version 16 or higher)
- npm or yarn package manager

### Setup Instructions

1. **Clone or download the project**
   ```bash
   cd social-media-app
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

4. **Open your browser**
   Navigate to `http://localhost:3000`

## 🔐 Demo Credentials

For testing purposes, you can use these demo accounts:

**Existing User:**
- Email: `john@example.com`
- Password: `password`

**Or create a new account** using the registration form.

## 📱 Features Overview

### Authentication
- Secure login and registration
- Form validation and error handling
- Persistent login sessions
- Password visibility toggle

### Home Feed
- Personalized conversation feed
- Start new conversations with rich text
- Image upload support (UI ready)
- Real-time like and comment interactions
- Responsive conversation cards

### User Profiles
- Complete user profiles with cover images
- Bio, location, and social links
- Follower/following counts
- User's conversation history
- Follow/unfollow functionality

### Social Features
- Like conversations with heart animation
- Comment on conversations with threaded discussions
- Share conversations (UI ready)
- Follow other users
- Real-time notifications (UI ready)

### Responsive Design
- Mobile-first approach
- Collapsible sidebar navigation
- Touch-friendly interactions
- Optimized for all screen sizes

## 🎨 Customization

### Styling
The app uses Tailwind CSS with a custom design system. You can customize:

- **Colors**: Modify `tailwind.config.js` to change the color palette
- **Components**: Update component styles in `src/index.css`
- **Layout**: Adjust the layout components for different designs

### Adding Features
The codebase is well-structured for easy extension:

- **New Pages**: Add to `src/pages/`
- **Components**: Add to `src/components/`
- **Types**: Define in `src/types/index.ts`
- **Hooks**: Add custom hooks to `src/hooks/`

## 🚀 Deployment

### Build for Production
```bash
npm run build
```

This creates an optimized production build in the `build` folder.

### Deploy to Vercel
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow the prompts

### Deploy to Netlify
1. Build the project: `npm run build`
2. Upload the `build` folder to Netlify
3. Configure redirects for client-side routing

## 🔧 Development

### Project Structure
```
src/
├── components/          # Reusable UI components
│   ├── Layout.tsx      # Main layout wrapper
│   ├── PostCard.tsx    # Individual post component
│   └── CreatePost.tsx  # Post creation form
├── pages/              # Page components
│   ├── Home.tsx        # Main feed page
│   ├── Login.tsx       # Login page
│   ├── Register.tsx    # Registration page
│   └── Profile.tsx     # User profile page
├── contexts/           # React contexts
│   └── AuthContext.tsx # Authentication context
├── types/              # TypeScript type definitions
│   └── index.ts        # Main types file
├── hooks/              # Custom React hooks
├── utils/              # Utility functions
├── App.tsx             # Main app component
├── index.tsx           # App entry point
└── index.css           # Global styles
```

### Available Scripts

- `npm start` - Start development server
- `npm run build` - Build for production
- `npm test` - Run tests
- `npm run eject` - Eject from Create React App

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the console for error messages
2. Ensure all dependencies are installed
3. Verify Node.js version compatibility
4. Check the browser developer tools

## 🔮 Future Enhancements

- Real-time messaging
- Video post support
- Advanced search functionality
- Push notifications
- Dark mode toggle
- Post scheduling
- Analytics dashboard
- API integration
- Database persistence

---

**Built with ❤️ using React, TypeScript, and Tailwind CSS**
