type CardProps = {

  title: string;

  children: React.ReactNode;

};


export default function Card(
  {
    title,
    children
  }: CardProps
) {

  return (

    <section>

      <h2>
        {title}
      </h2>

      <div>
        {children}
      </div>

    </section>

  );

}
