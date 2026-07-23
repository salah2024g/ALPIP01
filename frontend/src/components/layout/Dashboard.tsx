export default function Dashboard(
  {
    children
  }: {
    children: React.ReactNode
  }
) {

  return (

    <div>

      <header>
        ALPIP Dashboard
      </header>


      <main>

        {children}

      </main>


    </div>

  );

}
