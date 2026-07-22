import { Outlet, Link } from "react-router-dom";

function Layout() {
  return (
    <>
      <nav className="bg-slate-900 text-white px-8 py-4 flex gap-6 shadow-lg">
        <Link className="hover:text-cyan-400" to="/">
          Home
        </Link>

        <Link className="hover:text-cyan-400" to="/profiles">
          Profiles
        </Link>
      </nav>

      {/* React Router Outlet */}
      <Outlet />
    </>
  );
}

export default Layout;