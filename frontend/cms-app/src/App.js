import './App.css';
import Navbar from "./components/Navbar";
import HeroSection from "./components/HeroSection";
import PlayersSection from "./components/PlayersSection";
import TournamentsSection from "./components/TournamentsSection";
import TournamentTypesSection from "./components/TournamentTypesSection";
import FanInteractionSection from "./components/FanInteractionSection";
import Footer from "./components/Footer";

const App = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <HeroSection />
      <PlayersSection />
      <TournamentsSection />
      <TournamentTypesSection />
      <FanInteractionSection />
      <Footer />
    </div>
  );
};

export default App;