const Navbar = () => {
  return (
    <nav className="bg-blue-900 text-white px-6 py-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">Cricket Management</h1>
      <ul className="flex gap-6">
        <li><a href="#" className="hover:underline">Home</a></li>
        <li><a href="#" className="hover:underline">Matches</a></li>
        <li><a href="#" className="hover:underline">Tournaments</a></li>
        <li><a href="#" className="hover:underline">Login</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;